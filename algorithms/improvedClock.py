# algorithms/improvedClock.py

from pageReplacement import PageReplacement
from page import Page

class ImprovedClock(PageReplacement):
    def __init__(self, page_table_size):
        super().__init__(page_table_size)
        self.pointer = 0  # 指针，模拟时钟指针
        self.pages_in_memory = []  # 页表

    def access_page(self, page_number, access_method):
        """
        访问页面，使用 Improved Clock 算法
        """
        # 查找页面是否已在内存中
        page_in_memory = next((page for page in self.pages_in_memory if page.page_number == page_number), None)

        if page_in_memory:
            # 如果页面已经在内存中，更新访问方法和引用位
            page_in_memory.access_method = access_method
            page_in_memory.status_bits['referenced'] = True
        else:
            # 如果页面不在内存中，触发缺页中断
            self.page_faults += 1
            if len(self.pages_in_memory) < self.page_table_size:
                # 空间足够，直接添加
                new_page = Page(page_number)
                new_page.access_method = access_method
                self.pages_in_memory.append(new_page)
            else:
                # 页表已满，进行页面替换
                while True:
                    page_to_replace = self.pages_in_memory[self.pointer]
                    if not page_to_replace.status_bits['referenced'] and not page_to_replace.status_bits['dirty']:
                        # 找到一个没有被引用且没有脏的页面，进行替换
                        self.pages_in_memory[self.pointer] = Page(page_number)
                        self.pages_in_memory[self.pointer].access_method = access_method
                        break
                    elif not page_to_replace.status_bits['referenced']:
                        # 如果页面没有被引用但被标记为脏，优先写回磁盘
                        page_to_replace.status_bits['dirty'] = False  # 重置脏位
                        self.pointer = (self.pointer + 1) % self.page_table_size  # 移动指针继续查找
                    else:
                        # 设置该页面的引用位为 0，并移动指针
                        page_to_replace.status_bits['referenced'] = False
                        self.pointer = (self.pointer + 1) % self.page_table_size

        # 显示当前页表
        self.display_page_table()