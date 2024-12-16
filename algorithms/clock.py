from pageReplacement import PageReplacement

class Clock(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)
        self.pointer = 0  # 时钟指针

    def access_page(self, page):
        if len(self.frames) < self.num_frames:
            if self.get_page(page.page_number) is None:
                page.physical_block = len(self.frames)  # 分配物理块号
                self.frames.append(page)
                page.valid = True
                print(f"Page {page.page_number} caused a page fault and was added to memory.")
            else:
                print(f"Page {page.page_number} is already in memory.")
        else:
            # 按时钟算法进行页面替换
            while True:
                current_page = self.frames[self.pointer]
                if current_page.valid:
                    current_page.valid = False  # 清除访问位
                    self.pointer = (self.pointer + 1) % self.num_frames
                else:
                    evicted = self.frames[self.pointer]
                    page.physical_block = evicted.physical_block  # 继承被替换页面的物理块号
                    self.frames[self.pointer] = page
                    page.valid = True
                    self.pointer = (self.pointer + 1) % self.num_frames
                    print(f"Page {page.page_number} caused a page fault and replaced page {evicted.page_number}.")
                    break
        self.print_page_table()

    def print_page_table(self):
        print("Current Page Table:")
        for frame in self.frames:
            print(frame)