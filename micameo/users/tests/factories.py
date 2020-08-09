from typing import Any, Sequence

import factory.fuzzy
from django.contrib.auth import get_user_model
from factory import (DjangoModelFactory, Faker,
                     post_generation, )

from micameo.users.models import Category, Talent, SubCategory, Client


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()
        django_get_or_create = ('username',)

    username = Faker("user_name")
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).generate(extra_kwargs={})
        )
        self.set_password(password)


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('name',)

    # name = factory.Sequence(lambda n: "Category %0d" % n)

    name = factory.Iterator([
        "Category1", "Category2", "Category3",
        "Category4", "Category5", "Category6", "Category7"
    ])


class SubCategoryFactory(DjangoModelFactory):
    class Meta:
        model = SubCategory
        django_get_or_create = ('sub_name',)

    sub_name = factory.Iterator([
        "Actor", "Influencer", "Youtuber",
        "Atleta", "Futbolista", "Beisbolista", "Cantante"
    ])
    category = factory.SubFactory(CategoryFactory)


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)


class TalentFactory(DjangoModelFactory):
    class Meta:
        model = Talent
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory)
    description = Faker(
        'paragraph', nb_sentences=8, variable_nb_sentences=True
    )
    profile_image = 'https://picsum.photos/400/400'

    @post_generation
    def post(self, create, extracted, **kwargs):
        category = SubCategoryFactory()
        self.categories.set((category,))
        # if not create:
        #     # Simple build, do nothing.
        #     return
        # if extracted:
        #     self.cacategories.set(Category())
