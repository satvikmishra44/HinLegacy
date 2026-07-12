from hinlegacy.detector import detect_font
from hinlegacy.detector.heuristics import score_fonts

sample = "Dr f=k vk pkS"
print(detect_font(sample))
print(score_fonts(sample))