from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class PlayerPageNumberPagination(PageNumberPagination):
    page_size = 10


class PlayerLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10
