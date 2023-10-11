from django.core.management.base import BaseCommand
from shopping.models import Products, Choice

class Command(BaseCommand):
    """
    Custom Django management command to populate the Products and Choice models with initial data.
    """
        
    help = 'Populate the Products and Choice models with initial data'

    def handle(self, *args, **kwargs):

        """
        Handle the command execution.

        Deletes old data, creates Products and Choices for those Products.

        Args:
            *args: Additional arguments.
            **kwargs: Additional keyword arguments.
        """

        # delete old data
        Products.objects.all().delete()
        Choice.objects.all().delete()

        # Create Products
        product1 = Products.objects.create(
            question_text='The Sweater',
            price=400.00,
            image='products/sweater.jpg',
        )

        product2 = Products.objects.create(
            question_text='The Jacket',
            price=600.00,
            image='products/jacket.jpg',
        )

        product3 = Products.objects.create(
            question_text='The Jeans',
            price=650.00,
            image='products/jeans.jpg',
        )

        product4 = Products.objects.create(
            question_text='The Glasses',
            price=300.00,
            image='products/glasses.jpg',
        )

        product5 = Products.objects.create(
            question_text='The Hat',
            price=200.00,
            image='products/hat.jpg',
        )

        product6 = Products.objects.create(
            question_text='The Socks',
            price=300.00,
            image='products/socks.jpg',
        )

        # Create Choices for Products
        Choice.objects.create(
            question=product1,
            choice_text='Tygervalley',
        )

        Choice.objects.create(
            question=product1,
            choice_text='V&A Waterfront',
        )

        Choice.objects.create(
            question=product2,
            choice_text='Century City',
        )

        Choice.objects.create(
            question=product2,
            choice_text='V&A Waterfront',
        )

        Choice.objects.create(
            question=product3,
            choice_text='Tygervalley',
        )

        Choice.objects.create(
            question=product3,
            choice_text='V&A Waterfront',
        )
        Choice.objects.create(
            question=product3,
            choice_text='Century City',
        )
        Choice.objects.create(
            question=product4,
            choice_text='V&A Waterfront',
        )
        Choice.objects.create(
            question=product4,
            choice_text='Century City',
        )

        Choice.objects.create(
            question=product5,
            choice_text='V&A Waterfront',
        )

        Choice.objects.create(
            question=product5,
            choice_text='Century City',
        )

        Choice.objects.create(
            question=product6,
            choice_text='Tygervalley',
        )

        Choice.objects.create(
            question=product6,
            choice_text='V&A Waterfront',
        )
        self.stdout.write(self.style.SUCCESS('Data populated successfully.'))
