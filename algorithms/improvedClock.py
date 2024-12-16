from pageReplacement import PageReplacement
from page import Page

class ImprovedClock(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)
        self.pointer = 0  # 指针初始化为0

    def access_page(self, page):
        existing_page = self.get_page(page.page_number)
        if existing_page:
            existing_page.reference_bit = 1  # 设置引用位
            existing_page.modified_bit = page.modified_bit  # 更新修改位
            existing_page.valid = True
            print(f"Page {page.page_number} is already in memory.")
        else:
            if len(self.frames) < self.num_frames:
                # 内存未满，直接添加页面
                page.physical_block = len(self.frames)  # 分配物理块号
                self.frames.append(page)
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and was added to memory.")
            else:
                while True:
                    current_page = self.frames[self.pointer]
                    if current_page.reference_bit == 0 and current_page.modified_bit == 0:
                        # 找到引用位和修改位都为0的页面，进行替换
                        page.physical_block = current_page.physical_block  # 继承被替换页面的物理块号
                        self.frames[self.pointer] = page
                        page.valid = True
                        self.pointer = (self.pointer + 1) % self.num_frames
                        print(f"Page {page.page_number} caused a page fault and replaced page {current_page.page_number}.")
                        break
                    elif current_page.reference_bit == 0 and current_page.modified_bit == 1:
                        # 找到引用位为0但修改位为1的页面，清除修改位
                        current_page.modified_bit = 0
                    else:
                        # 引用位为1的页面，清除引用位
                        current_page.reference_bit = 0
                    self.pointer = (self.pointer + 1) % self.num_frames
        self.print_page_table()

    def print_page_table(self):
        print("Current Page Table:")
        for frame in self.frames:
            print(frame)
