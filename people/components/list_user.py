from django.core.paginator import Paginator, EmptyPage
from django_unicorn.components import UnicornView

from people.models import CustomUser


class ListUserView(UnicornView):
    items_per_page = 5
    page_index = 1
    paginator = None
    page = None
    page_range = None

    class Meta:
        exclude = ()
        javascript_exclude = (
            "paginator",
            "page",
            "page_range",
        )

    users = []
    users_show_form = False

    category = ''
    categories = []

    users_search_flag = False

    def mount(self):
        self.users_list()

    def users_list(self):
        self.page = ''
        qs = CustomUser.objects.all()
        paginator = Paginator(qs, self.items_per_page)
        self.paginator = paginator
        self.page = self.paginator.page(self.page_index)
        self.page_range = self.paginator.get_elided_page_range(number=self.page_index, on_each_side=3, on_ends=2)
        return self.page



    def go_to_page(self, page):
        print(f"go_to_page {page}")
        self.page_index = page
        self.users_list()

    def users_search_button(self):
        self.page_index = 1
        self.users_search_flag = True
        self.users_search()

    def users_search(self):
        self.page = ''
        qs = CustomUser.objects.filter(email=self.email)
        paginator = Paginator(qs, self.items_per_page)
        self.paginator = paginator
        try:
            self.page = paginator.page(self.page_index)
            self.page_range = self.paginator.get_elided_page_range(number=self.page_index, on_each_side=3, on_ends=2)
            return self.page
        except EmptyPage:
            self.page = ''

    # def change_limit(self):
    #     user_list = CustomUser.objects.all()
    #     paginator = Paginator(user_list, self.page)
    #     try:
    #         blogs = paginator.page(self.page)
    #     except PageNotAnInteger:
    #         blogs = paginator.page(1)
    #     except EmptyPage:
    #         blogs = paginator.page(paginator.num_pages)
    #
    #     self.page_list = blogs.paginator.page_range
