from abc import ABC, abstractmethod

class PageReplacement(ABC):
    def __init__(self, num_frames):
        self.num_frames = num_frames  # 内存中可以存放的最大页面数
        self.frames = []  # 存储页面的列表

    @abstractmethod
    def access_page(self, page):
        pass

    def get_page(self, page_number):
        """返回页号对应的页面对象"""
        for page in self.frames:
            if page.page_number == page_number:
                return page
        return None