from pageReplacement import PageReplacement

class Clock(PageReplacement):
    def __init__(self, num_frames):
        super().__init__(num_frames)
        self.pointer = 0  # 时钟指针

    def access_page(self, page):
        if len(self.frames) < self.num_frames:
            if self.get_page(page.page_number) is None:
                self.frames.append(page)
            page.valid = True
        else:
            # 按时钟算法进行页面替换
            while True:
                current_page = self.frames[self.pointer]
                if current_page.valid:
                    current_page.valid = False  # 清除访问位
                    self.pointer = (self.pointer + 1) % self.num_frames
                else:
                    evicted = self.frames[self.pointer]
                    self.frames[self.pointer] = page
                    page.valid = True
                    self.pointer = (self.pointer + 1) % self.num_frames
                    break