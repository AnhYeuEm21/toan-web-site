# -*- coding: utf-8 -*-
"""
build_toan_sites.py - TRÌNH TỔNG HỢP WEB TOÁN 11 KẾT NỐI TRI THỨC
Tạo ra 2 phiên bản độc lập:
1. index.html - Bản Desktop siêu cấp với Sidebar TOC, ScrollSpy, Cheatsheet, Flashcards, Quizzes
2. mobile.html - Bản Mobile chuẩn ứng dụng với Top Appbar, Bottom Nav, Sliding Drawer
"""
import os
import sys

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from data_b0_lop10 import B0_LOP10_CONTENT
from data_b1_b2 import B1_CONTENT, B2_CONTENT
from data_b3_b4 import B3_CONTENT, B4_CONTENT
from data_b5 import B5_CONTENT
from data_h10_h11 import H10_CONTENT, H11_CONTENT
from data_h12_h13 import H12_CONTENT, H13_CONTENT

# ============================================================
# FLASHCARDS DATA CHO CÁC PHẦN
# ============================================================
FC_B0 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Tầng 0 (Chạm vào thẻ để lật đáp án)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; BÀI THƠ LỚP 10</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Sin, Cos, Tan, Cot trong tam giác vuông tính thế nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; THẦN CHÚ BẤT HỦ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>Sin Đi Học</strong> (Đối/Huyền)<br><strong>Cos Khóc Cười</strong> (Kề/Huyền)<br><strong>Tan Đoàn Kết</strong> (Đối/Kề)<br><strong>Cot Kết Đoàn</strong> (Kề/Đối)</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; ĐỊNH LÝ COSIN</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Công thức tính cạnh a trong tam giác thường khi biết b, c và góc A?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; PYTAGO MỞ RỘNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>a<sup>2</sup> = b<sup>2</sup> + c<sup>2</sup> &minus; 2bc &times; cos A</strong></p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; ĐƯỜNG TRUNG BÌNH</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Đường trung bình trong tam giác có tính chất gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; VŨ KHÍ HÌNH HỌC 11</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Nối trung điểm 2 cạnh bên: <strong>Song song với đáy và bằng &frac12; đáy</strong> (MN &parallel; BC và MN = &frac12; BC).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; TRỌNG TÂM G</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Trọng tâm tam giác chia đường trung tuyến theo tỉ lệ nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TỈ LỆ 2/3</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>AG/AM = 2/3</strong> và <strong>GM/AM = 1/3</strong> (trong đó M là trung điểm cạnh đối diện).</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B1 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 1 (Chạm vào thẻ để lật đáp án)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; DẤU 4 GÓC PHẦN TƯ</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Câu thần chú xét dấu 4 góc phần tư là gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; THẦN CHÚ VÀNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>"Nhất Cả &ndash; Nhì Sin &ndash; Tam Tan &ndash; Tứ Cos"</strong><br>(Phần tư I: tất cả dương; II: chỉ Sin dương; III: chỉ Tan/Cot dương; IV: chỉ Cos dương).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; GÓC LIÊN KẾT</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Bốn câu thần chú góc liên kết đặc biệt?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 4 CÂU THƠ BẤT HỦ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>Cos đối &ndash; Sin bù &ndash; Phụ chéo &ndash; Hơn kém pi tan cot</strong><br>(Thằng nào được đọc tên thì giữ dấu, còn lại mang dấu trừ).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; ĐỘ DÀI CUNG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Công thức tính độ dài cung tròn l theo bán kính R và góc &alpha;?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; l = R &times; &alpha;</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>l = R &times; &alpha;</strong> (Bắt buộc &alpha; phải đổi sang đơn vị <strong>radian</strong>, không được để độ!).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; HỆ THỨC CƠ BẢN</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">1 + tan<sup>2</sup>&alpha; bằng bao nhiêu?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 1 / cos<sup>2</sup>&alpha;</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>1 + tan<sup>2</sup>&alpha; = 1 / cos<sup>2</sup>&alpha;</strong><br>Và: <strong>1 + cot<sup>2</sup>&alpha; = 1 / sin<sup>2</sup>&alpha;</strong>.</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B2 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 2 (Chạm vào thẻ để lật đáp án)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; CÔNG THỨC CỘNG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Cos(a + b) và Sin(a + b) khai triển ra sao?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; THƠ CỘNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>cos(a + b) = cos a cos b &minus; sin a sin b</strong> (Cos đổi dấu)<br><strong>sin(a + b) = sin a cos b + cos a sin b</strong> (Sin giữ dấu)</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; BA MẶT COS 2A</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Ba công thức của cos 2a là gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 3 BIẾN THỂ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">1) <strong>cos<sup>2</sup>a &minus; sin<sup>2</sup>a</strong><br>2) <strong>2cos<sup>2</sup>a &minus; 1</strong><br>3) <strong>1 &minus; 2sin<sup>2</sup>a</strong></p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; CÔNG THỨC HẠ BẬC</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Hạ bậc sin<sup>2</sup>a và cos<sup>2</sup>a?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; COS CỘNG - SIN TRỪ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>cos<sup>2</sup>a = (1 + cos 2a) / 2</strong><br><strong>sin<sup>2</sup>a = (1 &minus; cos 2a) / 2</strong></p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; TỔNG THÀNH TÍCH</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">cos u &minus; cos v bằng gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TRỪ HAI SIN SIN</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>&minus;2 sin((u + v)/2) sin((u &minus; v)/2)</strong><br>(Nhớ phải có dấu TRỪ đằng trước!).</p>
      </div>
    </div>
  </div>
</div>
"""

FC_B4 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Bài 4 (Chạm vào thẻ để lật đáp án)</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; NGHIỆM PHƯƠNG TRÌNH SIN</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">sin x = sin &alpha; có 2 họ nghiệm nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; CHÍNH NÓ & PI TRỪ NÓ</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>x = &alpha; + k2&pi;</strong><br><strong>x = &pi; &minus; &alpha; + k2&pi;</strong> (k &isin; &Zopf;)</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; NGHIỆM PHƯƠNG TRÌNH COS</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">cos x = cos &alpha; có nghiệm là gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; CỘNG TRỪ ALPHA</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>x = &plusmn;&alpha; + k2&pi;</strong> (k &isin; &Zopf;)</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; ĐUÔI CỦA TAN VÀ COT</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Đuôi nghiệm của tan x = tan &alpha; là gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; CỘNG k&pi;</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);"><strong>x = &alpha; + k&pi;</strong> (Chỉ là k&pi; chứ không phải k2&pi;!).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; VÔ NGHIỆM</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Phương trình sin x = m vô nghiệm khi nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; |m| > 1</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Khi <strong>m &gt; 1</strong> hoặc <strong>m &lt; &minus;1</strong> (|m| &gt; 1) là lập tức kết luận VÔ NGHIỆM!</p>
      </div>
    </div>
  </div>
</div>
"""

FC_H10_H11 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Hình Không Gian Bài 10 - 11</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; TÌM GIAO TUYẾN</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Quy tắc vàng để tìm giao tuyến của 2 mặt phẳng?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TÌM 2 ĐIỂM CHUNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Tìm <strong>2 điểm chung phân biệt</strong> rồi nối lại. Giao tuyến chính là đường thẳng đi qua 2 điểm chung đó!</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; ĐƯỜNG THẲNG CHÉO NHAU</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Thế nào là hai đường thẳng chéo nhau?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; KHÔNG ĐỒNG PHẲNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Là hai đường thẳng <strong>không cùng nằm trong bất kì mặt phẳng nào</strong> (vừa không cắt nhau, vừa không song song).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; GIAO TUYẾN SONG SONG</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Nếu (P) chứa a, (Q) chứa b và a &parallel; b thì giao tuyến của chúng thế nào?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; SONG SONG a VÀ b</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Giao tuyến d của (P) và (Q) (nếu có) sẽ <strong>song song với cả a và b</strong>!</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; TỨ DIỆN</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Tứ diện ABCD có bao nhiêu cặp cạnh chéo nhau?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 3 CẶP ĐỐI DIỆN</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Có đúng <strong>3 cặp</strong>: (AB - CD), (AC - BD), (AD - BC).</p>
      </div>
    </div>
  </div>
</div>
"""

FC_H12_H13 = """
<div style="margin:24px 0 10px;">
  <h4 class="sub-title">🎴 Flashcard Lật Thẻ Ôn Nhanh Hình Không Gian Bài 12 - 13</h4>
  <div class="flashcard-deck">
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 1 &bull; CHỨNG MINH d &parallel; (P)</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Làm sao để chứng minh đường thẳng d song song mặt phẳng (P)?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 3 DÒNG VÀNG</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">1) d &not;&sub; (P)<br>2) d' &sub; (P)<br>3) <strong>d &parallel; d' &rArr; d &parallel; (P)</strong></p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 2 &bull; CHỨNG MINH (P) &parallel; (Q)</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Làm sao để chứng minh 2 mặt phẳng song song?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; 2 ĐƯỜNG CẮT NHAU</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Mặt phẳng (P) chứa <strong>hai đường thẳng cắt nhau</strong> a và b cùng song song với (Q) &rArr; (P) &parallel; (Q).</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 3 &bull; MẶT BÊN LĂNG TRỤ</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Các mặt bên của hình lăng trụ luôn là hình gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; HÌNH BÌNH HÀNH</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Luôn luôn là <strong>HÌNH BÌNH HÀNH</strong>, các cạnh bên song song và bằng nhau!</p>
      </div>
    </div>
    <div class="flashcard" onclick="flipCard(this)">
      <div class="fc-front">
        <div style="font-size:0.7rem;color:var(--text-muted);font-weight:700;">THẺ 4 &bull; ĐƯỜNG CHÉO HÌNH HỘP</div>
        <div style="font-size:0.95rem;font-weight:700;margin:10px 0;color:var(--accent-blue-light);">Bốn đường chéo của hình hộp có tính chất gì?</div>
        <div style="font-size:0.75rem;color:var(--accent-yellow);">👆 Chạm để lật xem đáp án</div>
      </div>
      <div class="fc-back" style="display:none;">
        <div style="font-size:0.7rem;color:var(--accent-green);font-weight:700;">ĐÁP ÁN &bull; TÂM HÌNH HỘP</div>
        <p style="font-size:0.86rem;margin-top:6px;color:var(--text-primary);">Cắt nhau tại <strong>trung điểm của mỗi đường</strong> (tâm đối xứng của hình hộp).</p>
      </div>
    </div>
  </div>
</div>
"""

# ============================================================
# CSS FLASHCARD & GIAO DIỆN DÙNG CHUNG
# ============================================================
FLASHCARD_CSS = """
/* FLASHCARD DECK */
.flashcard-deck {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 12px;
  margin: 14px 0 20px;
}
.flashcard {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius);
  padding: 16px;
  cursor: pointer;
  transition: transform 0.25s, border-color 0.25s, background 0.25s;
  user-select: none;
  min-height: 125px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.flashcard:hover {
  border-color: var(--accent-blue);
  transform: translateY(-2px);
}
.flashcard.flipped {
  background: rgba(105,240,174,0.08);
  border-color: var(--accent-green);
}
"""

COMMON_JS = """
// ============================================================
// HỆ THỐNG RENDER TOÁN HỌC KATEX & FALLBACK
// ============================================================
function triggerKaTeX(container) {
  var target = container || document.body;
  if (typeof renderMathInElement !== 'undefined') {
    renderMathInElement(target, {
      delimiters: [
        {left: '$$', right: '$$', display: true},
        {left: '$', right: '$', display: false}
      ],
      throwOnError: false,
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code"]
    });
  }
}

function initMathRender() {
  var retries = 0;
  var interval = setInterval(function() {
    retries++;
    if (typeof renderMathInElement !== 'undefined') {
      clearInterval(interval);
      triggerKaTeX(document.body);
    } else if (retries > 30) {
      clearInterval(interval);
      fallbackMathRender();
    }
  }, 100);
}

function fallbackMathRender() {
  var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
  var nodesToReplace = [];
  while (walker.nextNode()) {
    var node = walker.currentNode;
    if (node.parentElement && ['SCRIPT', 'STYLE', 'TEXTAREA', 'PRE', 'CODE'].indexOf(node.parentElement.tagName) === -1) {
      if (node.nodeValue.indexOf('$') !== -1) {
        nodesToReplace.push(node);
      }
    }
  }
  nodesToReplace.forEach(function(node) {
    var span = document.createElement('span');
    span.innerHTML = node.nodeValue.replace(/\\$([^$]+)\\$/g, function(match, formula) {
      var f = formula
        .replace(/\\\\alpha/g, '&alpha;')
        .replace(/\\\\beta/g, '&beta;')
        .replace(/\\\\pi/g, '&pi;')
        .replace(/\\\\sin/g, 'sin')
        .replace(/\\\\cos/g, 'cos')
        .replace(/\\\\tan/g, 'tan')
        .replace(/\\\\cot/g, 'cot')
        .replace(/\\\\parallel/g, '&parallel;')
        .replace(/\\\\subset/g, '&sub;')
        .replace(/\\\\in/g, '&isin;')
        .replace(/\\\\mathbb\\{R\\}/g, 'ℝ')
        .replace(/\\\\mathbb\\{Z\\}/g, 'ℤ')
        .replace(/\\\\mathbb\\{N\\}\\^?\\*?/g, 'ℕ*')
        .replace(/\\\\Rightarrow/g, '&rArr;')
        .replace(/\\\\Leftrightarrow/g, '&hArr;')
        .replace(/\\\\pm/g, '&plusmn;')
        .replace(/\\\\le/g, '&le;')
        .replace(/\\\\ge/g, '&ge;')
        .replace(/\\\\ne/g, '&ne;')
        .replace(/\\\\approx/g, '&approx;')
        .replace(/\\\\text\\{([^}]+)\\}/g, '$1')
        .replace(/\\\\mathbf\\{([^}]+)\\}/g, '<strong>$1</strong>')
        .replace(/\\\\frac\\{([^}]+)\\}\\{([^}]+)\\}/g, '<span class="fraction"><span class="num">$1</span><span class="den">$2</span></span>')
        .replace(/\\^\\\\circ/g, '&deg;');
      return '<span class="inline-math" style="font-family:var(--font-mono);font-weight:600;color:var(--accent-yellow);">' + f + '</span>';
    });
    node.parentNode.replaceChild(span, node);
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initMathRender);
} else {
  initMathRender();
}

// Quản lý Accordion
function toggleAcc(btn) {
  btn.classList.toggle('open');
  var content = btn.nextElementSibling;
  content.classList.toggle('open');
  if (content.classList.contains('open')) {
    triggerKaTeX(content);
  }
}

// Ẩn/hiện đáp án
function toggleAnswer(btn) {
  var ans = btn.nextElementSibling;
  ans.classList.toggle('visible');
  if (ans.classList.contains('visible')) {
    btn.innerText = '🙈 Thu gọn lời giải';
    triggerKaTeX(ans);
  } else {
    btn.innerText = '🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu làm ẩu!';
  }
}

// Lật thẻ Flashcard
function flipCard(card) {
  card.classList.toggle('flipped');
  var front = card.querySelector('.fc-front');
  var back = card.querySelector('.fc-back');
  if (card.classList.contains('flipped')) {
    front.style.display = 'none';
    back.style.display = 'block';
    triggerKaTeX(back);
  } else {
    front.style.display = 'block';
    back.style.display = 'none';
  }
}

// Modal xem ảnh SGK
function openSgkModal(filename) {
  var modal = document.getElementById('img-modal');
  var img = document.getElementById('img-modal-img');
  img.src = filename;
  modal.classList.add('open');
}

// Chọn Đúng / Sai
function selectTF(btn, val) {
  var parent = btn.parentElement;
  var btns = parent.querySelectorAll('.tf-btn');
  btns.forEach(function(b) { b.classList.remove('selected'); });
  btn.classList.add('selected');
  parent.dataset.selected = val;
}

// Chấm điểm Quiz cho từng bài
function gradeQuiz(lessonId) {
  var section = document.getElementById(lessonId + '-quiz');
  if (!section) return;

  var questions = section.querySelectorAll('.quiz-q');
  var score = 0;
  var total = questions.length;

  questions.forEach(function(q) {
    var type = q.dataset.type;
    var correctAns = q.dataset.ans;
    var explain = q.querySelector('.quiz-explain');

    if (type === 'mc') {
      var selected = q.querySelector('input[type="radio"]:checked');
      var options = q.querySelectorAll('.quiz-option');
      options.forEach(function(opt) {
        var radio = opt.querySelector('input');
        if (radio.value === correctAns) {
          opt.classList.add('correct');
        }
      });
      if (selected) {
        if (selected.value === correctAns) {
          score++;
        } else {
          selected.parentElement.classList.add('wrong');
        }
      }
      if (explain) {
        explain.classList.add('show');
        triggerKaTeX(explain);
      }
    } 
    else if (type === 'tf') {
      var tfContainer = q.querySelector('.tf-options');
      var userVal = tfContainer ? tfContainer.dataset.selected : null;
      var tfBtns = q.querySelectorAll('.tf-btn');
      tfBtns.forEach(function(b) {
        if (b.innerText.trim() === (correctAns === 'T' ? 'Đúng' : 'Sai')) {
          b.classList.add('correct');
        }
      });
      if (userVal === correctAns) {
        score++;
      } else if (userVal) {
        tfBtns.forEach(function(b) {
          if (b.classList.contains('selected') && !b.classList.contains('correct')) {
            b.classList.add('wrong');
          }
        });
      }
      if (explain) {
        explain.classList.add('show');
        triggerKaTeX(explain);
      }
    }
    else if (q.classList.contains('quiz-essay')) {
      var txt = q.querySelector('textarea');
      var sample = q.querySelector('.sample-answer');
      if (txt && txt.value.trim().length > 5) {
        score++;
      }
      if (sample) {
        sample.classList.add('show');
        triggerKaTeX(sample);
      }
    }
  });

  var badge = document.getElementById(lessonId + '-score');
  if (badge) {
    badge.style.display = 'inline-block';
    badge.innerText = 'Điểm của bạn: ' + score + '/' + total;
    if (score >= 12) {
      badge.style.background = 'rgba(105,240,174,0.2)';
      badge.style.borderColor = 'var(--accent-green)';
      alert('🎉 ĐỈNH CỦA CHÓP! Mày đạt ' + score + '/' + total + ' điểm. Mất gốc cái gì nữa, trình độ này đủ sức gánh cả lớp qua bài kiểm tra giữa kì rồi!');
    } else if (score >= 8) {
      badge.style.background = 'rgba(255,213,79,0.2)';
      badge.style.borderColor = 'var(--accent-yellow)';
      alert('⚡ KHÁ ỔN! Mày được ' + score + '/' + total + ' điểm. Đọc kĩ lại mấy câu giải thích màu đỏ để không bị lừa khi vào phòng thi nhé!');
    } else {
      badge.style.background = 'rgba(255,82,82,0.2)';
      badge.style.borderColor = 'var(--accent-red)';
      alert('⚠️ HƠI NGUY HIỂM! Mới được ' + score + '/' + total + ' điểm thôi. Xem lại mấy câu bị bẫy, đừng nản, làm lại lần nữa là nhớ vĩnh viễn!');
    }
  }
}

// Đổi Theme Dark/Light
var currentTheme = localStorage.getItem('toan11_theme') || 'dark';
document.documentElement.setAttribute('data-theme', currentTheme);

function toggleTheme() {
  currentTheme = currentTheme === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', currentTheme);
  localStorage.setItem('toan11_theme', currentTheme);
  updateThemeIcon();
}

function updateThemeIcon() {
  var btns = document.querySelectorAll('#theme-toggle, .btn-theme');
  btns.forEach(function(btn) {
    if (btn) btn.innerText = currentTheme === 'dark' ? '☀️' : '🌙';
  });
}
updateThemeIcon();

var tBtn = document.getElementById('theme-toggle');
if (tBtn) tBtn.addEventListener('click', toggleTheme);

// Progress Bar
window.addEventListener('scroll', function() {
  var h = document.documentElement;
  var b = document.body;
  var st = 'scrollTop';
  var sh = 'scrollHeight';
  var percent = (h[st]||b[st]) / ((h[sh]||b[sh]) - h.clientHeight) * 100;
  var pb = document.getElementById('progress-bar');
  if (pb) pb.style.width = percent + '%';
});

// ScrollSpy cho Sticky TOC trên Desktop
window.addEventListener('scroll', function() {
  var sections = document.querySelectorAll('.lesson-section');
  var scrollPos = window.scrollY + 140;
  var currentId = '';
  sections.forEach(function(sec) {
    if (sec.offsetTop <= scrollPos && (sec.offsetTop + sec.offsetHeight) > scrollPos) {
      currentId = sec.id;
    }
  });
  if (currentId) {
    document.querySelectorAll('.sidebar-nav .nav-item').forEach(function(item) {
      if (item.getAttribute('href') === '#' + currentId) {
        item.classList.add('active');
      } else {
        item.classList.remove('active');
      }
    });
  }
});
"""

# ============================================================
# BUILD INDEX.HTML (DESKTOP)
# ============================================================
def build_index_html():
    css_and_head = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Toán Học 11 – Kết Nối Tri Thức | Ôn Thi Cứu Nạn Mất Gốc</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">
<!-- KaTeX Math Rendering -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<style>
/* CSS VARIABLES */
:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-card: #21262d;
  --bg-hover: #292f39;
  --text-primary: #f0f6fc;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --accent-blue: #58a6ff;
  --accent-blue-light: #79c0ff;
  --accent-yellow: #f2cc60;
  --accent-yellow-dark: #d29922;
  --accent-red: #ff7b72;
  --accent-green: #7ee787;
  --accent-purple: #d2a8ff;
  --accent-orange: #ffa657;
  --border-color: #30363d;
  --border-bright: #484f58;
  --shadow: 0 4px 24px rgba(0,0,0,0.5);
  --shadow-lg: 0 8px 40px rgba(0,0,0,0.7);
  --radius: 12px;
  --radius-sm: 8px;
  --radius-lg: 16px;
  --sidebar-width: 290px;
  --font-main: 'Be Vietnam Pro', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --transition: all 0.25s ease;
}

[data-theme="light"] {
  --bg-primary: #f6f8fa;
  --bg-secondary: #ffffff;
  --bg-card: #ffffff;
  --bg-hover: #f3f4f6;
  --text-primary: #1f2328;
  --text-secondary: #57606a;
  --text-muted: #656d76;
  --accent-blue: #0969da;
  --accent-blue-light: #0550ae;
  --accent-yellow: #9a6700;
  --accent-yellow-dark: #7d4e00;
  --accent-red: #cf222e;
  --accent-green: #1a7f37;
  --accent-purple: #8250df;
  --accent-orange: #bc4c00;
  --border-color: #d0d7de;
  --border-bright: #afb8c1;
  --shadow: 0 4px 24px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 40px rgba(0,0,0,0.14);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; font-size: 16px; }
body {
  font-family: var(--font-main);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.75;
  overflow-x: hidden;
  transition: background 0.3s, color 0.3s;
}

/* MATH FRACTIONS & SUBSCRIPTS RESET */
sub, sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sub { bottom: -0.25em; }
sup { top: -0.5em; }

.fraction {
  display: inline-flex;
  flex-direction: column;
  vertical-align: middle;
  text-align: center;
  padding: 0 4px;
  line-height: 1.15;
  font-size: 0.95em;
}
.fraction .num {
  border-bottom: 2px solid currentColor;
  padding-bottom: 2px;
  margin-bottom: 2px;
  display: block;
}
.fraction .den {
  padding-top: 2px;
  display: block;
}

/* KATEX MATH RENDERING STYLES */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  margin: 12px 0;
  -webkit-overflow-scrolling: touch;
}
.katex {
  font-size: 1.05em;
  white-space: normal;
}
[data-theme="dark"] .katex {
  color: var(--text-primary);
}
[data-theme="light"] .katex {
  color: var(--text-primary);
}

#progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple), var(--accent-yellow));
  width: 0%; z-index: 9999;
}

.page-wrapper { display: flex; min-height: 100vh; }

/* SIDEBAR TOC */
#sidebar {
  position: fixed; top: 0; left: 0;
  width: var(--sidebar-width); height: 100vh;
  background: var(--bg-secondary);
  border-right: 1px solid var(--border-color);
  overflow-y: auto; z-index: 1000;
  transition: transform 0.3s ease;
  display: flex; flex-direction: column;
}
#sidebar.collapsed { transform: translateX(calc(-1 * var(--sidebar-width))); }

.sidebar-header {
  padding: 20px 16px 12px;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-card);
  position: sticky; top: 0; z-index: 1;
}
.sidebar-logo {
  font-size: 0.72rem; font-weight: 700; color: var(--text-muted);
  text-transform: uppercase; letter-spacing: 2px; margin-bottom: 4px;
}
.sidebar-title {
  font-size: 0.95rem; font-weight: 800; color: var(--accent-blue); line-height: 1.3;
}
.sidebar-nav { padding: 12px 0; flex: 1; }
.nav-section-label {
  padding: 10px 16px 4px; font-size: 0.65rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: 2px; color: var(--text-muted);
}
.nav-item {
  display: flex; align-items: center; gap: 8px;
  padding: 8px 16px; color: var(--text-secondary);
  text-decoration: none; font-size: 0.82rem; font-weight: 500;
  border-left: 3px solid transparent; transition: var(--transition);
}
.nav-item:hover { background: var(--bg-hover); color: var(--text-primary); border-left-color: var(--accent-blue); }
.nav-item.active { background: var(--bg-hover); color: var(--accent-blue); border-left-color: var(--accent-blue); font-weight: 700; }
.sidebar-footer { padding: 12px 16px; border-top: 1px solid var(--border-color); }

/* MAIN CONTENT */
#main-content {
  margin-left: var(--sidebar-width); flex: 1; min-width: 0;
  transition: margin-left 0.3s ease; padding: 0 0 80px;
}
#main-content.expanded { margin-left: 0; }

#topbar {
  position: sticky; top: 0; z-index: 900;
  background: var(--bg-secondary); border-bottom: 1px solid var(--border-color);
  padding: 12px 24px; display: flex; align-items: center; gap: 12px;
  backdrop-filter: blur(12px);
}
.topbar-title { font-size: 0.9rem; font-weight: 700; color: var(--text-primary); flex: 1; }
.btn-icon {
  width: 36px; height: 36px; border-radius: var(--radius-sm);
  border: 1px solid var(--border-color); background: var(--bg-card);
  color: var(--text-primary); cursor: pointer; display: flex;
  align-items: center; justify-content: center; font-size: 1.1rem;
  transition: var(--transition); flex-shrink: 0;
}
.btn-icon:hover { background: var(--accent-blue); border-color: var(--accent-blue); color: white; transform: scale(1.05); }

/* HERO */
.hero {
  background: linear-gradient(135deg, #0d1117 0%, #161b22 40%, #0d2136 100%);
  padding: 50px 32px; text-align: center; border-bottom: 1px solid var(--border-color);
}
[data-theme="light"] .hero {
  background: linear-gradient(135deg, #f6f8fa 0%, #e6edf3 40%, #ddf4ff 100%);
}
.hero-emoji { font-size: 3.5rem; margin-bottom: 14px; display: block; }
.hero h1 {
  font-size: 2.2rem; font-weight: 800;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  margin-bottom: 12px; line-height: 1.25;
}
.hero p { font-size: 1rem; color: var(--text-secondary); max-width: 700px; margin: 0 auto 24px; }
.hero-tags { display: flex; gap: 8px; justify-content: center; flex-wrap: wrap; }
.hero-tag {
  padding: 4px 14px; border-radius: 999px; font-size: 0.75rem; font-weight: 600;
  border: 1px solid;
}
.hero-tag.blue { background: rgba(88,166,255,0.15); border-color: var(--accent-blue); color: var(--accent-blue); }
.hero-tag.yellow { background: rgba(242,204,96,0.15); border-color: var(--accent-yellow); color: var(--accent-yellow); }
.hero-tag.green { background: rgba(126,231,135,0.15); border-color: var(--accent-green); color: var(--accent-green); }
.hero-tag.red { background: rgba(255,123,114,0.15); border-color: var(--accent-red); color: var(--accent-red); }

.content-area { max-width: 900px; margin: 0 auto; padding: 32px 24px; }
.lesson-section { margin-bottom: 60px; }
.lesson-header {
  display: flex; align-items: flex-start; gap: 16px; margin-bottom: 28px;
  padding-bottom: 20px; border-bottom: 2px solid var(--border-color);
}
.lesson-number {
  min-width: 56px; height: 56px;
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple));
  border-radius: var(--radius); display: flex; align-items: center;
  justify-content: center; font-size: 1.4rem; font-weight: 800; color: white;
  box-shadow: 0 4px 16px rgba(88,166,255,0.35); flex-shrink: 0;
}
.lesson-meta h2 { font-size: 1.55rem; font-weight: 800; color: var(--text-primary); margin-bottom: 6px; }
.lesson-meta .lesson-sub { font-size: 0.82rem; color: var(--text-muted); font-weight: 500; }
.lesson-tags { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 8px; }
.lesson-tag {
  padding: 2px 10px; border-radius: 999px; font-size: 0.7rem; font-weight: 600;
  background: var(--bg-hover); color: var(--text-secondary); border: 1px solid var(--border-color);
}

/* BOXES */
.box { border-radius: var(--radius); padding: 20px 24px; margin-bottom: 20px; border-left: 4px solid; }
.box-theory { background: rgba(88,166,255,0.08); border: 1px solid rgba(88,166,255,0.25); border-left: 4px solid var(--accent-blue); }
.box-theory .box-title { color: var(--accent-blue); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-formula { background: rgba(242,204,96,0.07); border: 1px solid rgba(242,204,96,0.3); border-left: 4px solid var(--accent-yellow); }
.box-formula .box-title { color: var(--accent-yellow); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-warning { background: rgba(255,123,114,0.07); border: 1px solid rgba(255,123,114,0.3); border-left: 4px solid var(--accent-red); }
.box-warning .box-title { color: var(--accent-red); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-story { background: rgba(126,231,135,0.07); border: 1px solid rgba(126,231,135,0.25); border-left: 4px solid var(--accent-green); }
.box-story .box-title { color: var(--accent-green); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }
.box-recall { background: rgba(210,168,255,0.07); border: 1px solid rgba(210,168,255,0.3); border-left: 4px solid var(--accent-purple); }
.box-recall .box-title { color: var(--accent-purple); font-size: 0.72rem; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 10px; }

/* FORMULA DISPLAY */
.formula-display {
  background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm);
  padding: 16px 20px; margin: 12px 0; font-family: var(--font-mono); font-size: 1.05rem;
  font-weight: 600; color: var(--accent-yellow); text-align: center; overflow-x: auto;
}
.formula-label { font-size: 0.72rem; color: var(--text-muted); text-align: center; margin-top: -8px; margin-bottom: 8px; font-weight: 500; }

/* ACCORDION */
.accordion-item { border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 8px; overflow: hidden; }
.accordion-trigger {
  width: 100%; background: var(--bg-card); border: none; padding: 14px 18px;
  color: var(--text-primary); font-family: var(--font-main); font-size: 0.9rem;
  font-weight: 600; text-align: left; cursor: pointer; display: flex;
  align-items: center; justify-content: space-between; gap: 12px;
}
.accordion-trigger:hover { background: var(--bg-hover); }
.accordion-trigger .acc-icon { font-size: 0.8rem; color: var(--text-muted); transition: transform 0.3s; }
.accordion-trigger.open .acc-icon { transform: rotate(180deg); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; background: var(--bg-secondary); }
.accordion-content.open { max-height: 3500px; }
.accordion-inner { padding: 16px 18px; }

/* TOOLTIP */
.tooltip { position: relative; cursor: help; border-bottom: 1px dashed var(--accent-blue); color: var(--accent-blue); font-weight: 600; }
.tooltip::after {
  content: attr(data-tip); position: absolute; bottom: calc(100% + 8px); left: 50%;
  transform: translateX(-50%); background: var(--bg-card); border: 1px solid var(--border-bright);
  color: var(--text-primary); padding: 8px 12px; border-radius: var(--radius-sm);
  font-size: 0.78rem; font-weight: 400; width: 220px; white-space: normal;
  text-align: center; box-shadow: var(--shadow); z-index: 100; opacity: 0;
  pointer-events: none; transition: opacity 0.2s; line-height: 1.5;
}
.tooltip:hover::after { opacity: 1; }

h3.sec-title { font-size: 1.15rem; font-weight: 700; color: var(--text-primary); margin: 28px 0 14px; display: flex; align-items: center; gap: 10px; }
h3.sec-title::before { content: ''; width: 4px; height: 20px; background: linear-gradient(180deg, var(--accent-blue), var(--accent-purple)); border-radius: 2px; }
h4.sub-title { font-size: 1rem; font-weight: 700; color: var(--text-secondary); margin: 20px 0 10px; padding-left: 12px; border-left: 3px solid var(--accent-blue); }

/* TABLE */
.tbl-wrap { overflow-x: auto; margin: 16px 0; border-radius: var(--radius-sm); }
table { width: 100%; border-collapse: collapse; font-size: 0.88rem; }
thead { background: var(--bg-hover); }
th { padding: 10px 14px; text-align: left; font-weight: 700; color: var(--text-secondary); font-size: 0.78rem; text-transform: uppercase; border-bottom: 2px solid var(--border-bright); }
td { padding: 9px 14px; border-bottom: 1px solid var(--border-color); color: var(--text-primary); }
tr:hover td { background: var(--bg-hover); }

/* STEP SOLVER */
.step-solver { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; margin: 16px 0; }
.step-solver-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 12px 18px; font-weight: 700; font-size: 0.9rem; color: white; }
.step-solver-body { padding: 16px 18px; }
.step { display: flex; gap: 14px; margin-bottom: 16px; align-items: flex-start; }
.step-num { min-width: 28px; height: 28px; background: var(--accent-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 800; color: white; }
.step-content { flex: 1; }
.step-content strong { color: var(--text-primary); font-size: 0.9rem; }
.step-content p { color: var(--text-secondary); font-size: 0.85rem; margin-top: 4px; }

.btn-reveal {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none;
  padding: 8px 20px; border-radius: 999px; font-family: var(--font-main); font-size: 0.82rem;
  font-weight: 700; cursor: pointer; transition: var(--transition); display: inline-flex; align-items: center; gap: 6px; margin-top: 10px;
}
.btn-reveal:hover { transform: translateY(-2px); box-shadow: 0 4px 16px rgba(88,166,255,0.4); }
.answer-content { display: none; margin-top: 12px; padding: 14px; background: rgba(126,231,135,0.08); border: 1px solid rgba(126,231,135,0.25); border-radius: var(--radius-sm); font-size: 0.88rem; line-height: 1.7; }
.answer-content.visible { display: block; }

/* SGK VIEWER */
.sgk-viewer { display: flex; gap: 8px; flex-wrap: wrap; margin: 16px 0; }
.sgk-btn {
  padding: 6px 14px; background: var(--bg-card); border: 1px solid var(--border-color);
  border-radius: var(--radius-sm); color: var(--text-secondary); font-family: var(--font-main);
  font-size: 0.78rem; font-weight: 600; cursor: pointer; transition: var(--transition);
  display: flex; align-items: center; gap: 6px;
}
.sgk-btn:hover { background: var(--accent-blue); border-color: var(--accent-blue); color: white; transform: translateY(-1px); }

/* MODALS */
#img-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 9998; align-items: center; justify-content: center; padding: 20px; }
#img-modal.open { display: flex; }
#img-modal img { max-width: 90vw; max-height: 90vh; border-radius: var(--radius); box-shadow: var(--shadow-lg); object-fit: contain; }
#img-modal-close { position: fixed; top: 20px; right: 20px; width: 40px; height: 40px; background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); border-radius: 50%; color: white; font-size: 1.2rem; cursor: pointer; display: flex; align-items: center; justify-content: center; }

#cheatsheet-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.85); z-index: 9997; overflow-y: auto; padding: 20px; }
#cheatsheet-modal.open { display: block; }
.cheatsheet-container { max-width: 750px; margin: 0 auto; background: var(--bg-card); border-radius: var(--radius-lg); border: 1px solid var(--border-color); overflow: hidden; }
.cheatsheet-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 20px 24px; display: flex; align-items: center; justify-content: space-between; color: white; }
.cheatsheet-header h3 { font-size: 1.1rem; font-weight: 800; }
.cheatsheet-header p { font-size: 0.78rem; opacity: 0.8; margin-top: 2px; }
.cheatsheet-body { padding: 20px 24px; }
.cheatsheet-section { margin-bottom: 20px; }
.cheatsheet-section h4 { font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border-color); }
.cs-formula { display: flex; align-items: flex-start; gap: 12px; padding: 8px 0; border-bottom: 1px solid var(--border-color); font-size: 0.85rem; }
.cs-f { font-family: var(--font-mono); color: var(--accent-yellow); font-weight: 600; min-width: 220px; }
.cs-d { color: var(--text-secondary); flex: 1; }

/* QUIZ */
.quiz-section { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-lg); padding: 24px; margin-top: 32px; }
.quiz-header { display: flex; align-items: center; gap: 12px; margin-bottom: 20px; padding-bottom: 16px; border-bottom: 1px solid var(--border-color); }
.quiz-icon { font-size: 1.8rem; }
.quiz-title { font-size: 1.1rem; font-weight: 800; color: var(--text-primary); }
.quiz-sub { font-size: 0.78rem; color: var(--text-muted); }
.quiz-score-badge { margin-left: auto; padding: 6px 14px; background: rgba(126,231,135,0.15); border: 1px solid var(--accent-green); border-radius: 999px; font-size: 0.82rem; font-weight: 700; color: var(--accent-green); display: none; }
.quiz-q { margin-bottom: 20px; padding: 16px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
.quiz-q-text { font-size: 0.9rem; font-weight: 600; color: var(--text-primary); margin-bottom: 12px; line-height: 1.6; }
.quiz-q-num { font-size: 0.7rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; margin-bottom: 6px; }
.quiz-options { display: flex; flex-direction: column; gap: 6px; }
.quiz-option { display: flex; align-items: center; gap: 10px; padding: 9px 14px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); cursor: pointer; font-size: 0.86rem; color: var(--text-secondary); background: var(--bg-card); transition: var(--transition); }
.quiz-option:hover { border-color: var(--accent-blue); color: var(--text-primary); background: rgba(88,166,255,0.08); }
.quiz-option.correct { border-color: var(--accent-green) !important; background: rgba(126,231,135,0.15) !important; color: var(--accent-green) !important; font-weight: 600; }
.quiz-option.wrong { border-color: var(--accent-red) !important; background: rgba(255,123,114,0.15) !important; color: var(--accent-red) !important; }
.quiz-explain { display: none; margin-top: 10px; padding: 10px 14px; background: rgba(126,231,135,0.08); border-radius: var(--radius-sm); font-size: 0.83rem; color: var(--text-secondary); border-left: 3px solid var(--accent-green); line-height: 1.6; }
.quiz-explain.show { display: block; }
.tf-options { display: flex; gap: 10px; }
.tf-btn { flex: 1; padding: 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-card); color: var(--text-secondary); font-family: var(--font-main); font-size: 0.86rem; font-weight: 600; cursor: pointer; transition: var(--transition); }
.tf-btn.selected { border-color: var(--accent-blue); background: rgba(88,166,255,0.12); color: var(--text-primary); }
.tf-btn.correct { border-color: var(--accent-green) !important; background: rgba(126,231,135,0.15) !important; color: var(--accent-green) !important; font-weight: 700; }
.tf-btn.wrong { border-color: var(--accent-red) !important; background: rgba(255,123,114,0.15) !important; color: var(--accent-red) !important; }
.quiz-essay textarea { width: 100%; min-height: 100px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 12px; color: var(--text-primary); font-family: var(--font-main); font-size: 0.86rem; resize: vertical; }
.quiz-essay .sample-answer { display: none; margin-top: 10px; padding: 12px; background: rgba(88,166,255,0.08); border-radius: var(--radius-sm); font-size: 0.84rem; color: var(--text-secondary); border-left: 3px solid var(--accent-blue); line-height: 1.6; }
.quiz-essay .sample-answer.show { display: block; }
.quiz-submit-btn { display: block; width: 100%; padding: 14px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none; border-radius: var(--radius); font-family: var(--font-main); font-size: 1rem; font-weight: 700; cursor: pointer; transition: var(--transition); margin-top: 20px; }
.quiz-submit-btn:hover { transform: translateY(-2px); box-shadow: 0 6px 24px rgba(88,166,255,0.4); }

""" + FLASHCARD_CSS + """
</style>
</head>
<body>
<div id="progress-bar"></div>

<div class="page-wrapper">
  <!-- SIDEBAR TOC -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-logo">TOÁN 11 KẾT NỐI TRI THỨC</div>
      <div class="sidebar-title">CỨU NẠN MẤT GỐC</div>
    </div>
    <nav class="sidebar-nav">
      <div class="nav-section-label">NỀN TẢNG CỐT LÕI</div>
      <a href="#tang-0" class="nav-item">🛡️ Tầng 0: Bảo bối Lớp 10</a>

      <div class="nav-section-label">CHƯƠNG I: LƯỢNG GIÁC</div>
      <a href="#bai-1" class="nav-item">📐 Bài 1: Giá trị lượng giác</a>
      <a href="#bai-2" class="nav-item">⚡ Bài 2: Công thức lượng giác</a>
      <a href="#bai-3" class="nav-item">📈 Bài 3: Hàm số lượng giác</a>
      <a href="#bai-4" class="nav-item">🎯 Bài 4: Phương trình lượng giác</a>

      <div class="nav-section-label">CHƯƠNG II: DÃY SỐ</div>
      <a href="#bai-5" class="nav-item">🔢 Bài 5: Dãy số</a>

      <div class="nav-section-label">CHƯƠNG IV: HÌNH KHÔNG GIAN</div>
      <a href="#bai-10" class="nav-item">📦 Bài 10: Đường & Mặt phẳng</a>
      <a href="#bai-11" class="nav-item">🛤️ Bài 11: Hai đường song song</a>
      <a href="#bai-12" class="nav-item">✈️ Bài 12: Đường // Mặt phẳng</a>
      <a href="#bai-13" class="nav-item">🏢 Bài 13: Hai mặt phẳng song song</a>
    </nav>
    <div class="sidebar-footer">
      <a href="mobile.html" style="display:block;text-align:center;padding:10px;background:rgba(88,166,255,0.12);border:1px solid var(--accent-blue);border-radius:var(--radius-sm);color:var(--accent-blue);text-decoration:none;font-size:0.8rem;font-weight:700;">📱 Xem Bản Điện Thoại</a>
    </div>
  </aside>

  <!-- MAIN CONTENT -->
  <main id="main-content">
    <div id="topbar">
      <button class="btn-icon" id="sidebar-toggle" onclick="document.getElementById('sidebar').classList.toggle('collapsed');document.getElementById('main-content').classList.toggle('expanded');">☰</button>
      <div class="topbar-title">Toán 11 &bull; Kết Nối Tri Thức &bull; Dành Cho Dân Mất Gốc</div>
      <button class="btn-icon" onclick="document.getElementById('cheatsheet-modal').classList.add('open')">📜</button>
      <button class="btn-icon" id="theme-toggle">☀️</button>
    </div>

    <!-- HERO SECTION -->
    <div class="hero">
      <span class="hero-emoji">📐</span>
      <h1>CHIẾN DỊCH CỨU NẠN TOÁN 11</h1>
      <p>Băm nát từng ngóc ngách sách giáo khoa sang tiếng người &bull; Giải thích cặn kẽ từ bảo bối lớp 10 &bull; Chinh phục điểm cao kiểm tra giữa kì!</p>
      <div class="hero-tags">
        <span class="hero-tag blue">Chương I: Lượng Giác</span>
        <span class="hero-tag yellow">Chương II: Dãy Số</span>
        <span class="hero-tag green">Chương IV: Hình Không Gian</span>
        <span class="hero-tag red">Bộ 105 Câu Trắc Nghiệm</span>
      </div>
    </div>

    <div class="content-area">
      <!-- TẦNG 0 -->
      """ + B0_LOP10_CONTENT + FC_B0 + """

      <!-- BÀI 1 -->
      """ + B1_CONTENT + FC_B1 + """

      <!-- BÀI 2 -->
      """ + B2_CONTENT + FC_B2 + """

      <!-- BÀI 3 -->
      """ + B3_CONTENT + """

      <!-- BÀI 4 -->
      """ + B4_CONTENT + FC_B4 + """

      <!-- BÀI 5 -->
      """ + B5_CONTENT + """

      <!-- BÀI 10 -->
      """ + H10_CONTENT + FC_H10_H11 + """

      <!-- BÀI 11 -->
      """ + H11_CONTENT + """

      <!-- BÀI 12 -->
      """ + H12_CONTENT + FC_H12_H13 + """

      <!-- BÀI 13 -->
      """ + H13_CONTENT + """
    </div>
  </main>
</div>

<!-- MODAL XEM ẢNH SGK -->
<div id="img-modal" onclick="if(event.target===this)this.classList.remove('open')">
  <button id="img-modal-close" onclick="document.getElementById('img-modal').classList.remove('open')">&times;</button>
  <img id="img-modal-img" src="" alt="Ảnh SGK">
</div>

<!-- CHEATSHEET MODAL -->
<div id="cheatsheet-modal" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="cheatsheet-container">
    <div class="cheatsheet-header">
      <div>
        <h3>📜 PHAO CỨU SINH TOÁN 11 SIÊU TỐC</h3>
        <p>Tổng hợp công thức ăn điểm trực tiếp trong bài thi giữa kì</p>
      </div>
      <button style="background:none;border:none;color:white;font-size:1.4rem;cursor:pointer;" onclick="document.getElementById('cheatsheet-modal').classList.remove('open')">&times;</button>
    </div>
    <div class="cheatsheet-body">
      <div class="cheatsheet-section">
        <h4>1. CÔNG THỨC LƯỢNG GIÁC CƠ BẢN</h4>
        <div class="cs-formula"><span class="cs-f">sin²&alpha; + cos²&alpha; = 1</span><span class="cs-d">Hệ thức Pytago lượng giác</span></div>
        <div class="cs-formula"><span class="cs-f">1 + tan²&alpha; = 1 / cos²&alpha;</span><span class="cs-d">&alpha; &ne; &pi;/2 + k&pi;</span></div>
        <div class="cs-formula"><span class="cs-f">1 + cot²&alpha; = 1 / sin²&alpha;</span><span class="cs-d">&alpha; &ne; k&pi;</span></div>
        <div class="cs-formula"><span class="cs-f">l = R &times; &alpha;</span><span class="cs-d">Độ dài cung (&alpha; tính bằng radian)</span></div>
      </div>

      <div class="cheatsheet-section">
        <h4>2. CÔNG THỨC CỘNG & NHÂN ĐÔI</h4>
        <div class="cs-formula"><span class="cs-f">cos(a &plusmn; b) = cos a cos b &mp; sin a sin b</span><span class="cs-d">Cos đổi dấu</span></div>
        <div class="cs-formula"><span class="cs-f">sin(a &plusmn; b) = sin a cos b &plusmn; cos a sin b</span><span class="cs-d">Sin giữ dấu</span></div>
        <div class="cs-formula"><span class="cs-f">sin 2a = 2sin a cos a</span><span class="cs-d">Nhân đôi sin</span></div>
        <div class="cs-formula"><span class="cs-f">cos 2a = 2cos²a &minus; 1 = 1 &minus; 2sin²a</span><span class="cs-d">3 dạng nhân đôi cos</span></div>
        <div class="cs-formula"><span class="cs-f">cos²a = (1 + cos 2a)/2 ; sin²a = (1 &minus; cos 2a)/2</span><span class="cs-d">Hạ bậc (Cos +, Sin &minus;)</span></div>
      </div>

      <div class="cheatsheet-section">
        <h4>3. PHƯƠNG TRÌNH LƯỢNG GIÁC CƠ BẢN</h4>
        <div class="cs-formula"><span class="cs-f">sin x = sin &alpha; &hArr; x = &alpha; + k2&pi; ; x = &pi; &minus; &alpha; + k2&pi;</span><span class="cs-d">Chính nó và &pi; trừ nó</span></div>
        <div class="cs-formula"><span class="cs-f">cos x = cos &alpha; &hArr; x = &plusmn;&alpha; + k2&pi;</span><span class="cs-d">Cộng trừ &alpha;</span></div>
        <div class="cs-formula"><span class="cs-f">tan x = tan &alpha; &hArr; x = &alpha; + k&pi;</span><span class="cs-d">Đuôi k&pi;</span></div>
      </div>

      <div class="cheatsheet-section">
        <h4>4. QUAN HỆ SONG SONG KHÔNG GIAN</h4>
        <div class="cs-formula"><span class="cs-f">d &parallel; d' &sub; (P) &rArr; d &parallel; (P)</span><span class="cs-d">Chứng minh đường // mặt</span></div>
        <div class="cs-formula"><span class="cs-f">a, b &sub; (P) cắt nhau; a, b &parallel; (Q) &rArr; (P) &parallel; (Q)</span><span class="cs-d">Chứng minh 2 mặt song song</span></div>
      </div>
    </div>
  </div>
</div>

<script>
""" + COMMON_JS + """
</script>
</body>
</html>
"""
    return css_and_head

# ============================================================
# BUILD MOBILE.HTML (PHIÊN BẢN DI ĐỘNG CHUẨN APP)
# ============================================================
def build_mobile_html():
    mobile_head = """<!DOCTYPE html>
<html lang="vi" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Toán 11 Mobile – Kết Nối Tri Thức</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap" rel="stylesheet">
<!-- KaTeX Math Rendering for Mobile -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"></script>
<style>
/* CSS VARIABLES FOR MOBILE */
:root {
  --bg-primary: #0d1117;
  --bg-secondary: #161b22;
  --bg-card: #21262d;
  --bg-hover: #292f39;
  --text-primary: #f0f6fc;
  --text-secondary: #8b949e;
  --text-muted: #6e7681;
  --accent-blue: #58a6ff;
  --accent-blue-light: #79c0ff;
  --accent-yellow: #f2cc60;
  --accent-yellow-dark: #d29922;
  --accent-red: #ff7b72;
  --accent-green: #7ee787;
  --accent-purple: #d2a8ff;
  --accent-orange: #ffa657;
  --border-color: #30363d;
  --border-bright: #484f58;
  --radius: 12px;
  --radius-sm: 8px;
  --font-main: 'Be Vietnam Pro', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

[data-theme="light"] {
  --bg-primary: #f6f8fa;
  --bg-secondary: #ffffff;
  --bg-card: #ffffff;
  --bg-hover: #f3f4f6;
  --text-primary: #1f2328;
  --text-secondary: #57606a;
  --text-muted: #656d76;
  --accent-blue: #0969da;
  --accent-blue-light: #0550ae;
  --accent-yellow: #9a6700;
  --accent-yellow-dark: #7d4e00;
  --accent-red: #cf222e;
  --accent-green: #1a7f37;
  --accent-purple: #8250df;
  --accent-orange: #bc4c00;
  --border-color: #d0d7de;
  --border-bright: #afb8c1;
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
html { scroll-behavior: smooth; font-size: 15px; }
body {
  font-family: var(--font-main);
  background: var(--bg-primary);
  color: var(--text-primary);
  line-height: 1.65;
  padding-top: 56px;
  padding-bottom: 70px;
  overflow-x: hidden;
}

/* MATH & FRACTION FOR MOBILE */
sub, sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sub { bottom: -0.25em; }
sup { top: -0.5em; }

.fraction {
  display: inline-flex;
  flex-direction: column;
  vertical-align: middle;
  text-align: center;
  padding: 0 4px;
  line-height: 1.15;
  font-size: 0.95em;
}
.fraction .num {
  border-bottom: 2px solid currentColor;
  padding-bottom: 2px;
  margin-bottom: 2px;
  display: block;
}
.fraction .den {
  padding-top: 2px;
  display: block;
}

/* KATEX MATH STYLING FOR MOBILE */
.katex-display {
  overflow-x: auto;
  overflow-y: hidden;
  padding: 6px 0;
  margin: 10px 0;
  -webkit-overflow-scrolling: touch;
}
.katex {
  font-size: 1.02em;
  white-space: normal;
}
[data-theme="dark"] .katex {
  color: var(--text-primary);
}
[data-theme="light"] .katex {
  color: var(--text-primary);
}

#progress-bar {
  position: fixed; top: 0; left: 0; height: 3px;
  background: linear-gradient(90deg, var(--accent-blue), var(--accent-purple), var(--accent-yellow));
  width: 0%; z-index: 9999;
}

/* TOP APP BAR */
.mobile-appbar {
  position: fixed; top: 0; left: 0; right: 0; height: 56px;
  background: var(--bg-secondary); border-bottom: 1px solid var(--border-color);
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 16px; z-index: 1000; backdrop-filter: blur(10px);
}
.appbar-title { font-size: 0.95rem; font-weight: 800; color: var(--accent-blue); display: flex; align-items: center; gap: 8px; }
.appbar-actions { display: flex; align-items: center; gap: 8px; }
.btn-m-icon {
  width: 38px; height: 38px; border-radius: var(--radius-sm);
  background: var(--bg-card); border: 1px solid var(--border-color);
  color: var(--text-primary); font-size: 1.1rem; display: flex;
  align-items: center; justify-content: center; cursor: pointer;
}

/* BOTTOM NAVIGATION BAR */
.mobile-bottom-nav {
  position: fixed; bottom: 0; left: 0; right: 0; height: 60px;
  background: var(--bg-secondary); border-top: 1px solid var(--border-color);
  display: flex; align-items: center; justify-content: space-around;
  z-index: 1000; padding: 4px 6px;
}
.m-nav-tab {
  display: flex; flex-direction: column; align-items: center; justify-content: center;
  color: var(--text-muted); text-decoration: none; font-size: 0.65rem; font-weight: 600;
  padding: 4px 8px; border-radius: var(--radius-sm); transition: all 0.2s; flex: 1;
}
.m-nav-tab .tab-icon { font-size: 1.2rem; margin-bottom: 2px; }
.m-nav-tab:hover, .m-nav-tab.active { color: var(--accent-blue); background: var(--bg-hover); }

/* SLIDING DRAWER MENU */
#drawer {
  position: fixed; inset: 0; background: rgba(0,0,0,0.7); z-index: 2000;
  opacity: 0; pointer-events: none; transition: opacity 0.3s;
}
#drawer.open { opacity: 1; pointer-events: auto; }
.drawer-content {
  position: absolute; top: 0; left: 0; bottom: 0; width: 280px;
  background: var(--bg-secondary); border-right: 1px solid var(--border-color);
  transform: translateX(-100%); transition: transform 0.3s cubic-bezier(0.1, 0.9, 0.2, 1);
  display: flex; flex-direction: column; padding: 20px 16px; overflow-y: auto;
}
#drawer.open .drawer-content { transform: translateX(0); }
.drawer-header { display: flex; align-items: center; justify-content: space-between; padding-bottom: 16px; border-bottom: 1px solid var(--border-color); margin-bottom: 14px; }
.drawer-item {
  display: flex; align-items: center; gap: 10px; padding: 10px 12px;
  border-radius: var(--radius-sm); color: var(--text-secondary);
  text-decoration: none; font-size: 0.88rem; font-weight: 600; margin-bottom: 4px;
}
.drawer-item:hover, .drawer-item.active { background: var(--bg-hover); color: var(--accent-blue); }

/* MOBILE CONTENT STYLING */
.mobile-container { padding: 16px 14px; }
.hero-m {
  background: linear-gradient(135deg, rgba(88,166,255,0.15), rgba(210,168,255,0.1));
  border: 1px solid var(--border-color); border-radius: var(--radius);
  padding: 20px 16px; text-align: center; margin-bottom: 20px;
}
.hero-m h1 { font-size: 1.35rem; font-weight: 800; color: var(--accent-blue); margin-bottom: 6px; }
.hero-m p { font-size: 0.82rem; color: var(--text-secondary); margin-bottom: 12px; }

.lesson-section { margin-bottom: 40px; }
.lesson-header { display: flex; gap: 12px; align-items: center; margin-bottom: 18px; padding-bottom: 14px; border-bottom: 2px solid var(--border-color); }
.lesson-number { width: 44px; height: 44px; border-radius: 10px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; color: white; flex-shrink: 0; }
.lesson-meta h2 { font-size: 1.15rem; font-weight: 800; color: var(--text-primary); line-height: 1.3; }
.lesson-meta .lesson-sub { font-size: 0.75rem; color: var(--text-muted); }

.box { border-radius: var(--radius); padding: 14px 16px; margin-bottom: 16px; border-left: 4px solid; }
.box-theory { background: rgba(88,166,255,0.08); border: 1px solid rgba(88,166,255,0.2); border-left: 4px solid var(--accent-blue); }
.box-theory .box-title { color: var(--accent-blue); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-formula { background: rgba(242,204,96,0.07); border: 1px solid rgba(242,204,96,0.25); border-left: 4px solid var(--accent-yellow); }
.box-formula .box-title { color: var(--accent-yellow); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-warning { background: rgba(255,123,114,0.07); border: 1px solid rgba(255,123,114,0.25); border-left: 4px solid var(--accent-red); }
.box-warning .box-title { color: var(--accent-red); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-story { background: rgba(126,231,135,0.07); border: 1px solid rgba(126,231,135,0.2); border-left: 4px solid var(--accent-green); }
.box-story .box-title { color: var(--accent-green); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; margin-bottom: 8px; }
.box-recall { background: rgba(210,168,255,0.07); border: 1px solid rgba(210,168,255,0.25); border-left: 4px solid var(--accent-purple); }
.box-recall .box-title { color: var(--accent-purple); font-size: 0.7rem; font-weight: 700; text-transform: uppercase; }

.formula-display {
  background: var(--bg-card); border: 1px solid var(--border-bright); border-radius: var(--radius-sm);
  padding: 12px 14px; margin: 10px 0; font-family: var(--font-mono); font-size: 0.92rem;
  font-weight: 600; color: var(--accent-yellow); text-align: center; overflow-x: auto;
}
.formula-label { font-size: 0.68rem; color: var(--text-muted); text-align: center; margin-top: -6px; margin-bottom: 6px; }

.accordion-item { border: 1px solid var(--border-color); border-radius: var(--radius-sm); margin-bottom: 8px; overflow: hidden; }
.accordion-trigger {
  width: 100%; background: var(--bg-card); border: none; padding: 12px 14px;
  color: var(--text-primary); font-family: var(--font-main); font-size: 0.84rem;
  font-weight: 600; text-align: left; cursor: pointer; display: flex;
  align-items: center; justify-content: space-between; gap: 8px;
}
.accordion-trigger.open .acc-icon { transform: rotate(180deg); }
.accordion-content { max-height: 0; overflow: hidden; transition: max-height 0.4s ease; background: var(--bg-secondary); }
.accordion-content.open { max-height: 3500px; }
.accordion-inner { padding: 12px 14px; }

.tbl-wrap { overflow-x: auto; margin: 12px 0; -webkit-overflow-scrolling: touch; border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
table { width: 100%; border-collapse: collapse; font-size: 0.8rem; }
thead { background: var(--bg-hover); }
th { padding: 8px 10px; text-align: left; font-weight: 700; color: var(--text-secondary); font-size: 0.7rem; text-transform: uppercase; white-space: nowrap; }
td { padding: 8px 10px; border-bottom: 1px solid var(--border-color); color: var(--text-primary); }

.step-solver { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); overflow: hidden; margin: 14px 0; }
.step-solver-header { background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); padding: 10px 14px; font-weight: 700; font-size: 0.85rem; color: white; }
.step-solver-body { padding: 12px 14px; }
.step { display: flex; gap: 10px; margin-bottom: 12px; align-items: flex-start; }
.step-num { min-width: 24px; height: 24px; background: var(--accent-blue); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.7rem; font-weight: 800; color: white; flex-shrink: 0; }
.step-content strong { color: var(--text-primary); font-size: 0.85rem; }
.step-content p { color: var(--text-secondary); font-size: 0.8rem; margin-top: 3px; }

.btn-reveal {
  background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none;
  padding: 8px 16px; border-radius: 999px; font-family: var(--font-main); font-size: 0.78rem;
  font-weight: 700; cursor: pointer; display: inline-flex; align-items: center; gap: 6px; margin-top: 8px;
}
.answer-content { display: none; margin-top: 10px; padding: 12px; background: rgba(126,231,135,0.08); border: 1px solid rgba(126,231,135,0.2); border-radius: var(--radius-sm); font-size: 0.82rem; }
.answer-content.visible { display: block; }

.sgk-viewer { display: flex; gap: 6px; overflow-x: auto; padding-bottom: 4px; margin: 12px 0; }
.sgk-btn { padding: 6px 10px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-sm); color: var(--text-secondary); font-size: 0.72rem; white-space: nowrap; }

/* QUIZ MOBILE */
.quiz-section { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius); padding: 16px; margin-top: 24px; }
.quiz-header { display: flex; align-items: center; gap: 10px; margin-bottom: 14px; padding-bottom: 12px; border-bottom: 1px solid var(--border-color); }
.quiz-icon { font-size: 1.5rem; }
.quiz-title { font-size: 0.95rem; font-weight: 800; color: var(--text-primary); }
.quiz-sub { font-size: 0.72rem; color: var(--text-muted); }
.quiz-score-badge { margin-left: auto; padding: 4px 10px; background: rgba(126,231,135,0.15); border: 1px solid var(--accent-green); border-radius: 999px; font-size: 0.75rem; font-weight: 700; color: var(--accent-green); display: none; }
.quiz-q { margin-bottom: 16px; padding: 12px; background: var(--bg-secondary); border-radius: var(--radius-sm); border: 1px solid var(--border-color); }
.quiz-q-text { font-size: 0.84rem; font-weight: 600; color: var(--text-primary); margin-bottom: 10px; line-height: 1.5; }
.quiz-q-num { font-size: 0.65rem; color: var(--text-muted); font-weight: 700; text-transform: uppercase; margin-bottom: 4px; }
.quiz-options { display: flex; flex-direction: column; gap: 6px; }
.quiz-option { display: flex; align-items: center; gap: 8px; padding: 8px 10px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.8rem; color: var(--text-secondary); background: var(--bg-card); }
.quiz-option.correct { border-color: var(--accent-green) !important; background: rgba(126,231,135,0.15) !important; color: var(--accent-green) !important; }
.quiz-option.wrong { border-color: var(--accent-red) !important; background: rgba(255,123,114,0.15) !important; color: var(--accent-red) !important; }
.quiz-explain { display: none; margin-top: 8px; padding: 8px 10px; background: rgba(126,231,135,0.08); border-radius: var(--radius-sm); font-size: 0.78rem; color: var(--text-secondary); border-left: 3px solid var(--accent-green); }
.quiz-explain.show { display: block; }
.tf-options { display: flex; gap: 8px; }
.tf-btn { flex: 1; padding: 8px; border-radius: var(--radius-sm); border: 1px solid var(--border-color); background: var(--bg-card); color: var(--text-secondary); font-size: 0.8rem; font-weight: 600; cursor: pointer; }
.tf-btn.selected { border-color: var(--accent-blue); background: rgba(88,166,255,0.12); color: var(--text-primary); }
.tf-btn.correct { border-color: var(--accent-green) !important; background: rgba(126,231,135,0.15) !important; color: var(--accent-green) !important; font-weight: 700; }
.tf-btn.wrong { border-color: var(--accent-red) !important; background: rgba(255,123,114,0.15) !important; color: var(--accent-red) !important; }
.quiz-essay textarea { width: 100%; min-height: 80px; background: var(--bg-card); border: 1px solid var(--border-color); border-radius: var(--radius-sm); padding: 10px; color: var(--text-primary); font-size: 0.8rem; }
.quiz-essay .sample-answer { display: none; margin-top: 8px; padding: 10px; background: rgba(88,166,255,0.08); border-radius: var(--radius-sm); font-size: 0.78rem; color: var(--text-secondary); border-left: 3px solid var(--accent-blue); }
.quiz-essay .sample-answer.show { display: block; }
.quiz-submit-btn { width: 100%; padding: 12px; background: linear-gradient(135deg, var(--accent-blue), var(--accent-purple)); color: white; border: none; border-radius: var(--radius-sm); font-size: 0.9rem; font-weight: 700; margin-top: 16px; }

/* MODAL SGK */
#img-modal { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 9998; align-items: center; justify-content: center; padding: 12px; }
#img-modal.open { display: flex; }
#img-modal img { max-width: 95vw; max-height: 85vh; border-radius: var(--radius-sm); object-fit: contain; }
#img-modal-close { position: fixed; top: 14px; right: 14px; width: 36px; height: 36px; background: rgba(255,255,255,0.2); border: none; border-radius: 50%; color: white; font-size: 1.2rem; display: flex; align-items: center; justify-content: center; }

""" + FLASHCARD_CSS + """
</style>
</head>
<body>
<div id="progress-bar"></div>

<!-- TOP APP BAR -->
<header class="mobile-appbar">
  <button class="btn-m-icon" onclick="document.getElementById('drawer').classList.add('open')">☰</button>
  <div class="appbar-title">📐 TOÁN 11 KẾT NỐI</div>
  <div class="appbar-actions">
    <button class="btn-m-icon btn-theme" onclick="toggleTheme()">☀️</button>
  </div>
</header>

<!-- SLIDING DRAWER -->
<div id="drawer" onclick="if(event.target===this)this.classList.remove('open')">
  <div class="drawer-content">
    <div class="drawer-header">
      <div style="font-size:0.9rem;font-weight:800;color:var(--accent-blue);">MỤC LỤC BÀI HỌC</div>
      <button style="background:none;border:none;color:var(--text-muted);font-size:1.4rem;" onclick="document.getElementById('drawer').classList.remove('open')">&times;</button>
    </div>
    <a href="#tang-0" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">🛡️ Tầng 0: Nền Tảng Lớp 10</a>
    <div style="font-size:0.65rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;margin:10px 0 4px 12px;">ĐẠI SỐ & LƯỢNG GIÁC</div>
    <a href="#bai-1" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">📐 Bài 1: Giá Trị Lượng Giác</a>
    <a href="#bai-2" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">⚡ Bài 2: Công Thức Lượng Giác</a>
    <a href="#bai-3" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">📈 Bài 3: Hàm Số Lượng Giác</a>
    <a href="#bai-4" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">🎯 Bài 4: Phương Trình Lượng Giác</a>
    <a href="#bai-5" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">🔢 Bài 5: Dãy Số</a>
    <div style="font-size:0.65rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;margin:10px 0 4px 12px;">HÌNH HỌC KHÔNG GIAN</div>
    <a href="#bai-10" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">📦 Bài 10: Đường & Mặt Phẳng</a>
    <a href="#bai-11" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">🛤️ Bài 11: Hai Đường Song Song</a>
    <a href="#bai-12" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">✈️ Bài 12: Đường // Mặt Phẳng</a>
    <a href="#bai-13" class="drawer-item" onclick="document.getElementById('drawer').classList.remove('open')">🏢 Bài 13: Hai Mặt Song Song</a>
  </div>
</div>

<!-- BOTTOM NAVIGATION -->
<nav class="mobile-bottom-nav">
  <a href="#tang-0" class="m-nav-tab">
    <span class="tab-icon">🛡️</span>
    <span>Tầng 0</span>
  </a>
  <a href="#bai-1" class="m-nav-tab">
    <span class="tab-icon">📐</span>
    <span>Lượng Giác</span>
  </a>
  <a href="#bai-5" class="m-nav-tab">
    <span class="tab-icon">🔢</span>
    <span>Dãy Số</span>
  </a>
  <a href="#bai-10" class="m-nav-tab">
    <span class="tab-icon">📦</span>
    <span>Hình Học</span>
  </a>
</nav>

<!-- MAIN CONTENT FOR MOBILE -->
<main class="mobile-container">
  <div class="hero-m">
    <h1>CỨU NẠN TOÁN 11</h1>
    <p>Dành riêng cho người mất gốc &bull; Tối ưu lướt trên điện thoại</p>
    <a href="index.html" style="font-size:0.75rem;color:var(--accent-blue);font-weight:700;text-decoration:none;">💻 Chuyển sang Bản Máy Tính</a>
  </div>

  <!-- TẦNG 0 -->
  """ + B0_LOP10_CONTENT + FC_B0 + """

  <!-- BÀI 1 -->
  """ + B1_CONTENT + FC_B1 + """

  <!-- BÀI 2 -->
  """ + B2_CONTENT + FC_B2 + """

  <!-- BÀI 3 -->
  """ + B3_CONTENT + """

  <!-- BÀI 4 -->
  """ + B4_CONTENT + FC_B4 + """

  <!-- BÀI 5 -->
  """ + B5_CONTENT + """

  <!-- BÀI 10 -->
  """ + H10_CONTENT + FC_H10_H11 + """

  <!-- BÀI 11 -->
  """ + H11_CONTENT + """

  <!-- BÀI 12 -->
  """ + H12_CONTENT + FC_H12_H13 + """

  <!-- BÀI 13 -->
  """ + H13_CONTENT + """
</main>

<!-- MODAL SGK -->
<div id="img-modal" onclick="if(event.target===this)this.classList.remove('open')">
  <button id="img-modal-close" onclick="document.getElementById('img-modal').classList.remove('open')">&times;</button>
  <img id="img-modal-img" src="" alt="Ảnh SGK">
</div>

<script>
""" + COMMON_JS + """
</script>
</body>
</html>
"""
    return mobile_head

# ============================================================
# MAIN COMPILATION
# ============================================================
if __name__ == '__main__':
    desktop_html = build_index_html()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(desktop_html)
    print(f'DONE: Generated index.html successfully! Size: {len(desktop_html)} bytes')

    mobile_html = build_mobile_html()
    with open('mobile.html', 'w', encoding='utf-8') as f:
        f.write(mobile_html)
    print(f'DONE: Generated mobile.html successfully! Size: {len(mobile_html)} bytes')
