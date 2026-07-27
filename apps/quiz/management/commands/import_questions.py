import pandas as pd

from django.db import transaction
from django.core.management.base import BaseCommand

from apps.quiz.models import (
    Subject,
    Topic,
    Question,
    Choice,
)


class Command(BaseCommand):
    help = "Import questions from Excel"

    def add_arguments(self, parser):
        parser.add_argument("file", type=str)

    @transaction.atomic
    def handle(self, *args, **options):

        file = options["file"]

        questions_df = pd.read_excel(
            file,
            sheet_name="Questions",
            engine="openpyxl",
        )

        choices_df = pd.read_excel(
            file,
            sheet_name="Choices",
            engine="openpyxl",
        )

        created_count = 0
        updated_count = 0

        for _, row in questions_df.iterrows():

            subject, _ = Subject.objects.get_or_create(
                name=row["subject"],
                defaults={
                    "theme": "programming",
                },
            )

            topic, _ = Topic.objects.get_or_create(
                subject=subject,
                name=row["topic"],
            )

            question, created = Question.objects.update_or_create(
                external_id=row["question_id"],
                defaults={
                    "topic": topic,
                    "text": row["question"],
                    "code_snippet": "" if pd.isna(row["code"]) else row["code"],
                    "explanation": "" if pd.isna(row["explanation"]) else row["explanation"],
                    "difficulty": row["difficulty"],
                    "question_type": row["question_type"],
                    "marks": int(row["marks"]),
                    "is_active": True,
                },
            )

            question.choices.all().delete()

            current_choices = choices_df[
                choices_df["question_id"] == row["question_id"]
            ]


            for _, c in current_choices.iterrows():

                Choice.objects.create(
                    question=question,
                    text=c["choice"],
                    is_correct=bool(c["is_correct"]),
                    order=int(c["order"]),
                )

            if created:
                created_count += 1
            else:
                updated_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Created : {created_count}, Updated : {updated_count}"
            )
        )