# -*- coding: utf-8 -*-
"""
data_b3_b4.py - BÀI 3 & BÀI 4 (CHƯƠNG I ĐẠI SỐ 11)
Bao gồm:
- Bài 3: Hàm số lượng giác (SGK trang 22 - 31)
- Bài 4: Phương trình lượng giác cơ bản (SGK trang 32 - 40)
Kèm 15 câu trắc nghiệm kiểm tra độ hiểu bài cho từng bài.
"""

B3_CONTENT = r"""
<section class="lesson-section" id="bai-3">
  <div class="lesson-header">
    <div class="lesson-number">3</div>
    <div class="lesson-meta">
      <h2>BÀI 3: HÀM SỐ LƯỢNG GIÁC</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương I &bull; Trang 22 &ndash; 31</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Hàm số chẵn - lẻ</span>
        <span class="lesson-tag">Tính tuần hoàn & Chu kì</span>
        <span class="lesson-tag">Hàm số Sin, Cosin</span>
        <span class="lesson-tag">Hàm số Tang, Cotang</span>
        <span class="lesson-tag">Tập xác định & GTLN - GTNN</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('page_10.png')">📖 Xem SGK Trang 22-23</button>
    <button class="sgk-btn" onclick="openSgkModal('page_11.png')">📖 Xem SGK Trang 24-25</button>
    <button class="sgk-btn" onclick="openSgkModal('page_12.png')">📖 Xem SGK Trang 26-27</button>
    <button class="sgk-btn" onclick="openSgkModal('page_13.png')">📖 Xem SGK Trang 28-29</button>
    <button class="sgk-btn" onclick="openSgkModal('page_14.png')">📖 Xem SGK Trang 30-31</button>
  </div>

  <!-- PHẦN 1: HÀM SỐ CHẴN - LẺ & TUẦN HOÀN -->
  <h3 class="sec-title" id="b3-chan-le-tuan-hoan">1. "Dịch" Hàm Số Chẵn, Lẻ & Tuần Hoàn Sang Tiếng Người</h3>

  <div class="box box-theory">
    <div class="box-title">💡 PHÂN BIỆT HÀM CHẴN VÀ HÀM LẺ (BÍ QUYẾT ĐỐI XỨNG)</div>
    <p>Hiểu cực kì đơn giản: Cho số đối $-x$ vào máy xay hàm số $f(x)$:</p>
    <ul class="content-list">
      <li><strong>HÀM SỐ CHẴN:</strong> Cho $-x$ vào, nó nuốt chửng dấu trừ như không có chuyện gì xảy ra: <strong>$f(-x) = f(x)$</strong>.
        <br>&bull; <em>Tính chất hình học:</em> Đồ thị của hàm chẵn đối xứng nhau qua <strong>TRỤC TUNG (Oy)</strong> (giống như soi gương qua trục dọc).
      </li>
      <li><strong>HÀM SỐ LẺ:</strong> Cho $-x$ vào, nó nhổ dấu trừ ra đằng trước: <strong>$f(-x) = -f(x)$</strong>.
        <br>&bull; <em>Tính chất hình học:</em> Đồ thị của hàm lẻ đối xứng nhau qua <strong>GỐC TỌA ĐỘ O</strong> (lộn ngược $180^\circ$ qua tâm O).
      </li>
    </ul>
    <div class="formula-display" style="color:var(--accent-green);border-color:var(--accent-green);margin-top:10px;">
      QUY TẮC VÀNG 4 HÀM LƯỢNG GIÁC:<br>
      Duy nhất y = cos x là HÀM SỐ CHẴN!<br>
      Ba hàm còn lại: y = sin x, y = tan x, y = cot x ĐỀU LÀ HÀM SỐ LẺ!
    </div>
  </div>

  <div class="box box-theory">
    <div class="box-title">💡 HÀM SỐ TUẦN HOÀN & CHU KÌ LÀ GÌ?</div>
    <p>Hãy tưởng tượng nhịp tim đập, sóng biển vỗ bờ, hoặc chiếc đu quay Ferris. Cứ sau một khoảng thời gian cố định $T$, mọi hình ảnh, vị trí lại lặp lại y hệt như cũ!</p>
    <p style="margin-top:6px;">Số $T > 0$ nhỏ nhất để <strong>$f(x + T) = f(x)$</strong> được gọi là <strong>CHU KÌ</strong> của hàm số.</p>
    <ul class="content-list" style="margin-top:6px;">
      <li>$y = \sin x$ và $y = \cos x$ tuần hoàn với chu kì <strong>$T = 2\pi$</strong> ($360^\circ$).</li>
      <li>$y = \tan x$ và $y = \cot x$ tuần hoàn với chu kì <strong>$T = \pi$</strong> ($180^\circ$).</li>
      <li><strong>Công thức tổng quát cho đề thi:</strong>
        <br>&bull; $y = \sin(\omega x + \varphi)$ hoặc $y = \cos(\omega x + \varphi) \Rightarrow T = \frac{2\pi}{|\omega|}$.
        <br>&bull; $y = \tan(\omega x + \varphi)$ hoặc $y = \cot(\omega x + \varphi) \Rightarrow T = \frac{\pi}{|\omega|}$.
      </li>
    </ul>
  </div>

  <!-- PHẦN 2: MỔ XẺ 4 HÀM SỐ LƯỢNG GIÁC -->
  <h3 class="sec-title" id="b3-khao-sat-4-ham">2. Bảng So Sánh Toàn Diện 4 Hàm Số Lượng Giác</h3>

  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Đặc tính</th>
          <th>$y = \sin x$</th>
          <th>$y = \cos x$</th>
          <th>$y = \tan x$</th>
          <th>$y = \cot x$</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Tập xác định (D)</strong></td>
          <td>$D = \mathbb{R}$</td>
          <td>$D = \mathbb{R}$</td>
          <td>$D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi\}$</td>
          <td>$D = \mathbb{R} \setminus \{k\pi\}$</td>
        </tr>
        <tr>
          <td><strong>Tập giá trị (T)</strong></td>
          <td>$[-1; 1]$</td>
          <td>$[-1; 1]$</td>
          <td>$\mathbb{R}$ ($-\infty; +\infty$)</td>
          <td>$\mathbb{R}$ ($-\infty; +\infty$)</td>
        </tr>
        <tr>
          <td><strong>Tính chẵn / lẻ</strong></td>
          <td><span style="color:var(--accent-orange);font-weight:700;">Hàm số LẺ</span></td>
          <td><span style="color:var(--accent-green);font-weight:700;">Hàm số CHẴN</span></td>
          <td><span style="color:var(--accent-orange);font-weight:700;">Hàm số LẺ</span></td>
          <td><span style="color:var(--accent-orange);font-weight:700;">Hàm số LẺ</span></td>
        </tr>
        <tr>
          <td><strong>Chu kì (T)</strong></td>
          <td>$T = 2\pi$</td>
          <td>$T = 2\pi$</td>
          <td>$T = \pi$</td>
          <td>$T = \pi$</td>
        </tr>
        <tr>
          <td><strong>Đặc điểm biến thiên</strong></td>
          <td>Tăng giảm luân phiên</td>
          <td>Tăng giảm luân phiên</td>
          <td><span style="color:var(--accent-blue-light);font-weight:700;">LUÔN ĐỒNG BIẾN</span> trên từng khoảng xác định</td>
          <td><span style="color:var(--accent-red);font-weight:700;">LUÔN NGHỊCH BIẾN</span> trên từng khoảng xác định</td>
        </tr>
        <tr>
          <td><strong>Dạng đồ thị</strong></td>
          <td>Đường hình sin qua $O(0, 0)$</td>
          <td>Đường hình sin qua $(0, 1)$</td>
          <td>Nhánh uốn lượn đi lên</td>
          <td>Nhánh uốn lượn đi xuống</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- PHẦN 3: BÀI TOÁN TÌM TẬP XÁC ĐỊNH & GTLN - GTNN -->
  <h3 class="sec-title" id="b3-dang-toan-trong-tam">3. Hai Dạng Toán Chiếm 80% Đề Kiểm Tra Về Hàm Số Lượng Giác</h3>

  <div class="box box-warning">
    <div class="box-title">🔥 DẠNG 1: TÌM TẬP XÁC ĐỊNH CỦA HÀM SỐ (BẪY MẪU SỐ & CĂN BẬC HAI)</div>
    <p>Để tìm tập xác định, mày chỉ cần nhớ đúng 4 điều kiện cốt tử sau:</p>
    <ul class="content-list">
      <li>1) Phân thức có dạng $\frac{A}{B} \Rightarrow$ <strong>Điều kiện: Mẫu số $B \ne 0$</strong>.</li>
      <li>2) Biểu thức trong căn $\sqrt{A} \Rightarrow$ <strong>Điều kiện: Biểu thức $A \ge 0$</strong>.</li>
      <li>3) Hàm số chứa $\tan(u) \Rightarrow$ <strong>Điều kiện: $\cos(u) \ne 0 \Leftrightarrow u \ne \frac{\pi}{2} + k\pi$ ($k \in \mathbb{Z}$)</strong>.</li>
      <li>4) Hàm số chứa $\cot(u) \Rightarrow$ <strong>Điều kiện: $\sin(u) \ne 0 \Leftrightarrow u \ne k\pi$ ($k \in \mathbb{Z}$)</strong>.</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">🔥 DẠNG 2: TÌM GTLN (MAX) VÀ GTNN (MIN)</div>
    <p>Dựa trên sự thật thép: Sin và Cos luôn bị kẹp chặt giữa $-1$ và $1$:</p>
    <div class="formula-display">
      &minus;1 &le; sin(bất kì thứ gì) &le; 1   và   &minus;1 &le; cos(bất kì thứ gì) &le; 1
    </div>
    <p style="margin-top:8px;">Nếu bình phương lên: $0 \le \sin^2(u) \le 1$ và $0 \le \cos^2(u) \le 1$.</p>
    <p style="margin-top:6px;"><strong>Ví dụ:</strong> Tìm Max, Min của $y = 3\sin(2x - \frac{\pi}{3}) + 5$:</p>
    <p>&bull; Ta có: $-1 \le \sin(2x - \frac{\pi}{3}) \le 1$.</p>
    <p>&bull; Nhân 3 vào các vế: $-3 \le 3\sin(2x - \frac{\pi}{3}) \le 3$.</p>
    <p>&bull; Cộng thêm 5 vào các vế: $-3 + 5 \le y \le 3 + 5 \Rightarrow \mathbf{2 \le y \le 8}$.</p>
    <p>&bull; Vậy <strong>Min $y = 2$</strong> (khi $\sin = -1$) và <strong>Max $y = 8$</strong> (khi $\sin = 1$). Quá dễ nuốt!</p>
  </div>

  <!-- PHẦN 4: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 3 -->
  <div class="quiz-section" id="b3-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 3 (15 CÂU)</div>
        <div class="quiz-sub">Kiểm tra tập xác định, tính chẵn lẻ, chu kì, Max - Min &bull; Đạt 12/15 là giỏi!</div>
      </div>
      <div class="quiz-score-badge" id="b3-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Tập xác định của hàm số $y = \tan x$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q1" value="A"> A. $D = \mathbb{R}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q1" value="B"> B. $D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi, k \in \mathbb{Z}\}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q1" value="C"> C. $D = \mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q1" value="D"> D. $D = [-1; 1]$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\tan x = \frac{\sin x}{\cos x}$ xác định khi $\cos x \ne 0 \Leftrightarrow x \ne \frac{\pi}{2} + k\pi$. Chọn B.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hàm số nào sau đây là HÀM SỐ CHẴN?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q2" value="A"> A. $y = \cos x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q2" value="B"> B. $y = \sin x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q2" value="C"> C. $y = \tan x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q2" value="D"> D. $y = \cot x$</label>
      </div>
      <div class="quiz-explain">Giải thích: Trong 4 hàm lượng giác cơ bản, duy nhất $y = \cos x$ có $\cos(-x) = \cos x$ nên là hàm chẵn. Chọn A.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Chu kì tuần hoàn của hàm số $y = \sin 2x$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q3" value="A"> A. $2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b3_q3" value="B"> B. $4\pi$</label>
        <label class="quiz-option"><input type="radio" name="b3_q3" value="C"> C. $\pi$</label>
        <label class="quiz-option"><input type="radio" name="b3_q3" value="D"> D. $\frac{\pi}{2}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Công thức chu kì $T = \frac{2\pi}{|\omega|} = \frac{2\pi}{2} = \pi$. Chọn C.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Giá trị lớn nhất của hàm số $y = 4 - 3\cos x$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q4" value="A"> A. $1$</label>
        <label class="quiz-option"><input type="radio" name="b3_q4" value="B"> B. $4$</label>
        <label class="quiz-option"><input type="radio" name="b3_q4" value="C"> C. $3$</label>
        <label class="quiz-option"><input type="radio" name="b3_q4" value="D"> D. $7$</label>
      </div>
      <div class="quiz-explain">Giải thích: Ta có $-1 \le \cos x \le 1 \Rightarrow -3 \le -3\cos x \le 3 \Rightarrow 4 - 3 \le 4 - 3\cos x \le 4 + 3 \Rightarrow 1 \le y \le 7$. Giá trị lớn nhất là 7 (đạt được khi $\cos x = -1$). Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Tập xác định của hàm số $y = \frac{1}{\sin x}$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q5" value="A"> A. $D = \mathbb{R} \setminus \{\frac{\pi}{2} + k\pi\}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q5" value="B"> B. $D = \mathbb{R} \setminus \{k\pi, k \in \mathbb{Z}\}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q5" value="C"> C. $D = \mathbb{R}$</label>
        <label class="quiz-option"><input type="radio" name="b3_q5" value="D"> D. $D = \mathbb{R} \setminus \{0\}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Điều kiện mẫu $\sin x \ne 0 \Leftrightarrow x \ne k\pi$ ($k \in \mathbb{Z}$). Chọn B.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hàm số nào sau đây LUÔN ĐỒNG BIẾN trên mỗi khoảng xác định của nó?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q6" value="A"> A. $y = \sin x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q6" value="B"> B. $y = \cos x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q6" value="C"> C. $y = \tan x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q6" value="D"> D. $y = \cot x$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hàm số $y = \tan x$ luôn đồng biến trên mỗi khoảng $(-\frac{\pi}{2} + k\pi; \frac{\pi}{2} + k\pi)$. Trong khi $y = \cot x$ luôn nghịch biến. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Đồ thị hàm số $y = \cos x$ nhận đường thẳng nào làm trục đối xứng?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q7" value="A"> A. Trục tung $Oy$</label>
        <label class="quiz-option"><input type="radio" name="b3_q7" value="B"> B. Trục hoành $Ox$</label>
        <label class="quiz-option"><input type="radio" name="b3_q7" value="C"> C. Đường thẳng $y = x$</label>
        <label class="quiz-option"><input type="radio" name="b3_q7" value="D"> D. Gốc tọa độ $O$</label>
      </div>
      <div class="quiz-explain">Giải thích: Vì $y = \cos x$ là hàm số chẵn nên đồ thị của nó nhận trục tung Oy làm trục đối xứng. Chọn A.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Tập giá trị của hàm số $y = 3\sin x - 2$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b3_q8" value="A"> A. $[-3; 3]$</label>
        <label class="quiz-option"><input type="radio" name="b3_q8" value="B"> B. $[-1; 1]$</label>
        <label class="quiz-option"><input type="radio" name="b3_q8" value="C"> C. $[-2; 2]$</label>
        <label class="quiz-option"><input type="radio" name="b3_q8" value="D"> D. $[-5; 1]$</label>
      </div>
      <div class="quiz-explain">Giải thích: $-1 \le \sin x \le 1 \Rightarrow -3 \le 3\sin x \le 3 \Rightarrow -3 - 2 \le y \le 3 - 2 \Rightarrow -5 \le y \le 1$. Tập giá trị là $[-5; 1]$. Chọn D.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hàm số $y = \sin x$ và hàm số $y = \cos x$ đều có cùng tập giá trị là đoạn $[-1; 1]$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Với mọi $x \in \mathbb{R}$, ta luôn có $-1 \le \sin x \le 1$ và $-1 \le \cos x \le 1$.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Chu kì tuần hoàn của hàm số $y = \tan x$ là $2\pi$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Chu kì của $y = \tan x$ và $y = \cot x$ chỉ là $\pi$, còn chu kì của $y = \sin x$ và $y = \cos x$ mới là $2\pi$.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Đồ thị của hàm số $y = \sin x$ đi qua gốc tọa độ $O(0, 0)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tại $x = 0$ thì $y = \sin 0 = 0$, đồ thị đi qua gốc tọa độ $O(0, 0)$. Trong khi đó $\cos 0 = 1$ nên đồ thị cos đi qua $(0, 1)$.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hàm số $y = \cot x$ luôn đồng biến trên từng khoảng $(k\pi; \pi + k\pi)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Hàm số $y = \cot x$ LUÔN NGHỊCH BIẾN trên mỗi khoảng xác định của nó. Hàm $y = \tan x$ mới luôn đồng biến!</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hàm số $y = x^2 \cos x$ là hàm số chẵn. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! $f(-x) = (-x)^2 \cos(-x) = x^2 \cos x = f(x)$. Tích của hai hàm chẵn là một hàm chẵn!</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Tìm tập xác định</div>
      <div class="quiz-q-text">Tìm tập xác định của hàm số $y = \sqrt{\frac{1 + \cos x}{2 - \cos x}}$. Trình bày rõ lập luận điều kiện.</div>
      <textarea placeholder="Trình bày điều kiện xác định và kết luận tập D..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Điều kiện xác định: $\frac{1 + \cos x}{2 - \cos x} \ge 0$ và mẫu số $2 - \cos x \ne 0$.
        <br>&bull; Ta có với mọi $x \in \mathbb{R}$: $-1 \le \cos x \le 1$.
        <br>&bull; Tử số: $1 + \cos x \ge 0$ (luôn đúng).
        <br>&bull; Mẫu số: Vì $\cos x \le 1$ nên $2 - \cos x \ge 2 - 1 = 1 > 0$ (mẫu luôn dương với mọi $x$).
        <br>&bull; Do đó phân thức luôn có nghĩa và không âm với mọi $x \in \mathbb{R}$.
        <br>&bull; Kết luận: <strong>Tập xác định $D = \mathbb{R}$</strong>.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Vận tốc dòng khí hít thở của một người nghỉ ngơi được mô hình hóa bởi $v(t) = 0,85\sin(\frac{\pi}{3}t)$ (lít/giây). Tìm chu kì của một nhịp thở (thời gian từ lúc hít vào đến khi kết thúc thở ra) và thể tích khí tối đa lưu thông.</div>
      <textarea placeholder="Nhập chu kì T và vận tốc tối đa..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Tần số góc $\omega = \frac{\pi}{3}$ rad/s.
        <br>&bull; Chu kì của một chu trình hô hấp hoàn chỉnh: $T = \frac{2\pi}{\omega} = \frac{2\pi}{\pi / 3} = \mathbf{6\text{ giây}}$.
        <br>&bull; Vận tốc dòng khí đạt cực đại: $v_{\max} = 0,85 \times 1 = \mathbf{0,85\text{ lít/giây}}$.
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b3')">🏆 Chấm Điểm Bài 3 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""

B4_CONTENT = r"""
<section class="lesson-section" id="bai-4">
  <div class="lesson-header">
    <div class="lesson-number">4</div>
    <div class="lesson-meta">
      <h2>BÀI 4: PHƯƠNG TRÌNH LƯỢNG GIÁC CƠ BẢN</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương I &bull; Trang 32 &ndash; 40</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Phương trình sin x = m</span>
        <span class="lesson-tag">Phương trình cos x = m</span>
        <span class="lesson-tag">Phương trình tan x = m</span>
        <span class="lesson-tag">Phương trình cot x = m</span>
        <span class="lesson-tag">Trường hợp đặc biệt 0, 1, -1</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('page_14.png')">📖 Xem SGK Trang 32-33</button>
    <button class="sgk-btn" onclick="openSgkModal('page_15.png')">📖 Xem SGK Trang 34-35</button>
    <button class="sgk-btn" onclick="openSgkModal('page_16.png')">📖 Xem SGK Trang 36-37</button>
    <button class="sgk-btn" onclick="openSgkModal('page_17.png')">📖 Xem SGK Trang 38-39</button>
    <button class="sgk-btn" onclick="openSgkModal('page_18.png')">📖 Xem SGK Trang 40</button>
  </div>

  <!-- PHẦN 1: BẢN CHẤT GIẢI PHƯƠNG TRÌNH LƯỢNG GIÁC -->
  <h3 class="sec-title" id="b4-ban-chat">1. "Dịch" Phương Trình Lượng Giác Sang Tiếng Người</h3>

  <div class="box box-theory">
    <div class="box-title">💡 TẠI SAO PHƯƠNG TRÌNH LƯỢNG GIÁC LẠI CÓ "+ k2&pi;"?</div>
    <p>Hồi lớp 9 giải phương trình bậc nhất $2x - 4 = 0$ thì ra duy nhất $x = 2$. Xong chuyện.</p>
    <p style="margin-top:6px;">Nhưng khi giải $\sin x = 0,5$: Mày biết góc $30^\circ$ ($\frac{\pi}{6}$) có $\sin = 0,5$. Nhưng nếu cái kim quay thêm 1 vòng ($30^\circ + 360^\circ = 390^\circ$), nó lại dừng ở đúng vị trí đó và $\sin$ vẫn bằng $0,5$! Quay 2 vòng, 3 vòng, quay ngược 5 vòng... đều cho kết quả y hệt!</p>
    <p style="margin-top:6px;">Vì vậy, nghiệm lượng giác <strong>LUÔN LUÔN CÓ VÔ SỐ NGHIỆM</strong> và phải có cái đuôi <strong>$+ k2\pi$</strong> (hoặc $+ k360^\circ$) để đại diện cho $k$ vòng quay nguyên ($k \in \mathbb{Z}$)!</p>
  </div>

  <!-- PHẦN 2: BỐN BỘ CÔNG THỨC NGHIỆM CƠ BẢN -->
  <h3 class="sec-title" id="b4-4-cong-thuc">2. Bộ Tứ Công Thức Nghiệm Cơ Bản (Khắc Cốt Ghi Tâm)</h3>

  <div class="box box-formula">
    <div class="box-title">📐 1. PHƯƠNG TRÌNH sin x = m (ĐIỀU KIỆN CÓ NGHIỆM: |m| &le; 1)</div>
    <p>Nếu $|m| > 1$ (ví dụ $\sin x = 2$ hay $\sin x = -1,5$): <strong>KẾT LUẬN NGAY PHƯƠNG TRÌNH VÔ NGHIỆM!</strong> (vì $\sin$ chỉ chạy từ $-1$ đến $1$).</p>
    <p>Nếu $|m| \le 1$: Bấm máy `SHIFT SIN m` để tìm góc $\alpha$ sao cho $\sin\alpha = m$. Khi đó:</p>
    <div class="formula-display">
      sin x = sin &alpha;   &hArr;   
      <span style="display:inline-block;vertical-align:middle;text-align:left;">
        x = &alpha; + k2&pi;<br>
        x = &pi; &minus; &alpha; + k2&pi;
      </span>
      &nbsp;&nbsp;&nbsp;(k &isin; &Zopf;)
    </div>
    <div class="formula-label">Thần chú nhớ họ nghiệm sin: "MỘT HỌ LÀ CHÍNH NÓ &ndash; MỘT HỌ LÀ PI TRỪ NÓ" (nhớ câu "sin bù")</div>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 2. PHƯƠNG TRÌNH cos x = m (ĐIỀU KIỆN CÓ NGHIỆM: |m| &le; 1)</div>
    <p>Nếu $|m| > 1$: <strong>VÔ NGHIỆM!</strong></p>
    <p>Nếu $|m| \le 1$: Bấm máy `SHIFT COS m` ra góc $\alpha$. Khi đó:</p>
    <div class="formula-display">
      cos x = cos &alpha;   &hArr;   
      <span style="display:inline-block;vertical-align:middle;text-align:left;">
        x = &alpha; + k2&pi;<br>
        x = &minus;&alpha; + k2&pi;
      </span>
      &nbsp;&nbsp;&nbsp;(hoặc x = &plusmn;&alpha; + k2&pi;, k &isin; &Zopf;)
    </div>
    <div class="formula-label">Thần chú nhớ họ nghiệm cos: "CỘNG TRỪ ALPHA" (nhớ câu "cos đối")</div>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 3. PHƯƠNG TRÌNH tan x = m VÀ cot x = m (LUÔN CÓ NGHIỆM VỚI MỌI m &isin; R)</div>
    <p>Hàm tan và cot chạy từ $-\infty$ đến $+\infty$ nên bất kì số $m$ nào cũng có nghiệm! Đuôi chỉ là <strong>$+ k\pi$</strong> (chứ không phải $k2\pi$):</p>
    <div class="formula-display">
      tan x = tan &alpha;   &hArr;   x = &alpha; + k&pi;   (k &isin; &Zopf;)<br>
      cot x = cot &alpha;   &hArr;   x = &alpha; + k&pi;   (k &isin; &Zopf;)
    </div>
  </div>

  <!-- PHẦN 3: CÁC TRƯỜNG HỢP ĐẶC BIỆT 0, 1, -1 -->
  <h3 class="sec-title" id="b4-dac-biet">3. Ba Vị Trí Đặc Biệt (0, 1, -1) & Mẹo Gom Nghiệm</h3>

  <div class="box box-formula">
    <div class="box-title">📐 BẢNG GOM NGHIỆM ĐẶC BIỆT (CHỈ CÓ 1 HỌ NGHIỆM DUY NHẤT)</div>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Phương trình</th>
            <th>Bằng 0</th>
            <th>Bằng 1</th>
            <th>Bằng &minus;1</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$\sin x$</strong></td>
            <td><strong>$x = k\pi$</strong><br>(2 điểm cắt trục hoành)</td>
            <td><strong>$x = \frac{\pi}{2} + k2\pi$</strong><br>(đỉnh cao nhất trên cùng)</td>
            <td><strong>$x = -\frac{\pi}{2} + k2\pi$</strong><br>(đáy thấp nhất dưới cùng)</td>
          </tr>
          <tr>
            <td><strong>$\cos x$</strong></td>
            <td><strong>$x = \frac{\pi}{2} + k\pi$</strong><br>(2 điểm cắt trục tung)</td>
            <td><strong>$x = k2\pi$</strong><br>(điểm ngoài cùng bên phải)</td>
            <td><strong>$x = \pi + k2\pi$</strong><br>(điểm ngoài cùng bên trái)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:0.82rem;color:var(--text-muted);margin-top:8px;">💡 <strong>Mẹo sống còn:</strong> Khi bằng $\pm 1$ thì đuôi là <strong>$+ k2\pi$</strong> (vì chỉ có 1 điểm trên đường tròn). Khi bằng $0$ thì đuôi là <strong>$+ k\pi$</strong> (vì có 2 điểm đối xứng nhau qua tâm O)!</p>
  </div>

  <!-- PHẦN 4: THỰC CHIẾN BÀI 4 -->
  <h3 class="sec-title" id="b4-thuc-chien">4. Thực Chiến Giải Bài Tập Mẫu Bài 4 (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 1: GIẢI PHƯƠNG TRÌNH LƯỢNG GIÁC CHỨA BIỂU THỨC BẬC NHẤT</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Giải phương trình $2\sin(2x - \frac{\pi}{6}) - \sqrt{3} = 0$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Cô lập hàm sin về dạng cơ bản</strong>
          <p>$2\sin(2x - \frac{\pi}{6}) = \sqrt{3} \Leftrightarrow \sin(2x - \frac{\pi}{6}) = \frac{\sqrt{3}}{2}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Tìm góc đặc biệt bằng máy tính</strong>
          <p>Bấm `SHIFT SIN (√3 / 2)` ra góc $\frac{\pi}{3}$. Vậy phương trình trở thành:</p>
          <p>$\sin(2x - \frac{\pi}{6}) = \sin\frac{\pi}{3}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tách thành 2 họ nghiệm ("chính nó" và "pi trừ nó")</strong>
          <p>Trường hợp 1: $2x - \frac{\pi}{6} = \frac{\pi}{3} + k2\pi \Leftrightarrow 2x = \frac{\pi}{3} + \frac{\pi}{6} + k2\pi = \frac{\pi}{2} + k2\pi \Rightarrow \mathbf{x = \frac{\pi}{4} + k\pi}$.</p>
          <p>Trường hợp 2: $2x - \frac{\pi}{6} = \pi - \frac{\pi}{3} + k2\pi = \frac{2\pi}{3} + k2\pi \Leftrightarrow 2x = \frac{2\pi}{3} + \frac{\pi}{6} + k2\pi = \frac{5\pi}{6} + k2\pi \Rightarrow \mathbf{x = \frac{5\pi}{12} + k\pi}$ ($k \in \mathbb{Z}$).</p>
          <p><strong>Kết luận:</strong> Phương trình có 2 họ nghiệm chuẩn chỉ!</p>
        </div>
      </div>
    </div>
  </div>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 2: TÌM SỐ NGHIỆM THUỘC KHOẢNG [0; 2&pi;] (BẪY THI GIỮA KÌ)</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Tìm số nghiệm của phương trình $\cos 2x = 0$ trên đoạn $[0; 2\pi]$.</p>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem cách chặn k không bao giờ đếm sót!</button>
      <div class="answer-content">
        <p><strong>Bước 1: Giải nghiệm tổng quát</strong></p>
        <p>$\cos 2x = 0 \Leftrightarrow 2x = \frac{\pi}{2} + k\pi \Leftrightarrow x = \frac{\pi}{4} + k\frac{\pi}{2}$ ($k \in \mathbb{Z}$).</p>
        <p><strong>Bước 2: Cho nghiệm nằm trong đoạn $[0; 2\pi]$ để tìm k</strong></p>
        <p>$0 \le \frac{\pi}{4} + k\frac{\pi}{2} \le 2\pi$.</p>
        <p>Chia cả 3 vế cho $\pi$: $0 \le \frac{1}{4} + \frac{k}{2} \le 2$.</p>
        <p>Trừ $\frac{1}{4}$ cho cả 3 vế: $-\frac{1}{4} \le \frac{k}{2} \le \frac{7}{4}$.</p>
        <p>Nhân 2 cho cả 3 vế: $-0,5 \le k \le 3,5$.</p>
        <p>Vì $k \in \mathbb{Z}$ (số nguyên) nên $k$ chỉ có thể nhận các giá trị: <strong>$k \in \{0; 1; 2; 3\}$</strong>.</p>
        <p>Có 4 giá trị của $k \Rightarrow$ <strong>Phương trình có đúng 4 nghiệm</strong> trên đoạn $[0; 2\pi]$ (gồm: $\frac{\pi}{4}, \frac{3\pi}{4}, \frac{5\pi}{4}, \frac{7\pi}{4}$).</p>
      </div>
    </div>
  </div>

  <!-- PHẦN 5: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 4 -->
  <div class="quiz-section" id="b4-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 4 (15 CÂU)</div>
        <div class="quiz-sub">Đầy đủ 4 phương trình cơ bản, bấm máy Casio, chặn nghiệm trên đoạn &bull; Đạt 12/15 là qua môn!</div>
      </div>
      <div class="quiz-score-badge" id="b4-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Phương trình nào sau đây là VÔ NGHIỆM?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q1" value="A"> A. $\sin x = 0,5$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="B"> B. $\cos x = -1$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="C"> C. $\sin x = \sqrt{2}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="D"> D. $\tan x = 100$</label>
      </div>
      <div class="quiz-explain">Giải thích: Vì $-1 \le \sin x \le 1$ mà $\sqrt{2} \approx 1,414 > 1$ nên phương trình $\sin x = \sqrt{2}$ vô nghiệm. Chọn C.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nghiệm của phương trình $\cos x = 1$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q1" value="A"> A. $x = k2\pi, k \in \mathbb{Z}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="B"> B. $x = \pi + k2\pi, k \in \mathbb{Z}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="C"> C. $x = \frac{\pi}{2} + k\pi, k \in \mathbb{Z}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q1" value="D"> D. $x = k\pi, k \in \mathbb{Z}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Trên đường tròn lượng giác, điểm có $\cos = 1$ là điểm $A(1, 0)$, tương ứng $x = k2\pi$. Chọn A.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Tất cả các nghiệm của phương trình $\sin x = \sin\frac{\pi}{4}$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q3" value="A"> A. $x = \pm \frac{\pi}{4} + k2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="B"> B. $x = \frac{\pi}{4} + k2\pi$ và $x = \frac{3\pi}{4} + k2\pi$ ($k \in \mathbb{Z}$)</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="C"> C. $x = \frac{\pi}{4} + k\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q3" value="D"> D. $x = \frac{\pi}{4} + k2\pi$ và $x = -\frac{\pi}{4} + k2\pi$</label>
      </div>
      <div class="quiz-explain">Giải thích: Họ 1 là $x = \frac{\pi}{4} + k2\pi$; Họ 2 là $x = \pi - \frac{\pi}{4} + k2\pi = \frac{3\pi}{4} + k2\pi$. Chọn B.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nghiệm của phương trình $\tan x = 1$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q4" value="A"> A. $x = \frac{\pi}{4} + k2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="B"> B. $x = \pm \frac{\pi}{4} + k\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="C"> C. $x = \frac{\pi}{2} + k\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q4" value="D"> D. $x = \frac{\pi}{4} + k\pi, k \in \mathbb{Z}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\tan x = 1 = \tan\frac{\pi}{4} \Leftrightarrow x = \frac{\pi}{4} + k\pi$ ($k \in \mathbb{Z}$). Đuôi của tan luôn là $k\pi$! Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Phương trình $\cos x = 0$ có nghiệm là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q5" value="A"> A. $x = \frac{\pi}{2} + k\pi, k \in \mathbb{Z}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="B"> B. $x = k\pi, k \in \mathbb{Z}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="C"> C. $x = \frac{\pi}{2} + k2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q5" value="D"> D. $x = k2\pi$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos x = 0$ tại 2 điểm trên trục tung: $\frac{\pi}{2}$ và $-\frac{\pi}{2}$, gom nghiệm lại thành $x = \frac{\pi}{2} + k\pi$. Chọn A.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Giải phương trình $\sin 2x = -\frac{1}{2}$, ta được nghiệm là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q6" value="A"> A. $x = \pm \frac{\pi}{12} + k\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="B"> B. $x = -\frac{\pi}{6} + k\pi$ và $x = \frac{7\pi}{6} + k\pi$</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="C"> C. $x = -\frac{\pi}{12} + k\pi$ và $x = \frac{7\pi}{12} + k\pi$ ($k \in \mathbb{Z}$)</label>
        <label class="quiz-option"><input type="radio" name="b4_q6" value="D"> D. $x = -\frac{\pi}{12} + k2\pi$</label>
      </div>
      <div class="quiz-explain">Giải thích: $-\frac{1}{2} = \sin(-\frac{\pi}{6})$. $2x = -\frac{\pi}{6} + k2\pi \Rightarrow x = -\frac{\pi}{12} + k\pi$. Và $2x = \pi - (-\frac{\pi}{6}) + k2\pi = \frac{7\pi}{6} + k2\pi \Rightarrow x = \frac{7\pi}{12} + k\pi$. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Số nghiệm của phương trình $\sin x = 0$ trên đoạn $[0; 2\pi]$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q7" value="A"> A. $2$</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="B"> B. $3$</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="C"> C. $1$</label>
        <label class="quiz-option"><input type="radio" name="b4_q7" value="D"> D. $4$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\sin x = 0 \Leftrightarrow x = k\pi$. Với $x \in [0; 2\pi]$ ta có $k \in \{0, 1, 2\}$, tương ứng 3 nghiệm: $0, \pi, 2\pi$. Chọn B.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nghiệm âm lớn nhất của phương trình $\cos x = \frac{\sqrt{3}}{2}$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b4_q8" value="A"> A. $-\frac{\pi}{6}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="B"> B. $-\frac{\pi}{3}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="C"> C. $-\frac{5\pi}{6}$</label>
        <label class="quiz-option"><input type="radio" name="b4_q8" value="D"> D. $-\frac{11\pi}{6}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos x = \frac{\sqrt{3}}{2} \Leftrightarrow x = \pm \frac{\pi}{6} + k2\pi$. Nghiệm âm lớn nhất (gần số 0 nhất) là $-\frac{\pi}{6}$ (với họ trừ và $k=0$). Chọn A.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Phương trình $\cos x = m$ có nghiệm khi và chỉ khi $-1 \le m \le 1$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tập giá trị của cos là $[-1; 1]$, nếu $|m| > 1$ phương trình lập tức vô nghiệm.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Phương trình $\tan x = m$ luôn luôn có nghiệm với mọi giá trị $m \in \mathbb{R}$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tập giá trị của hàm tan là $\mathbb{R}$ nên bất kì số thực $m$ nào cũng tồn tại góc $\alpha$ thỏa mãn $\tan\alpha = m$.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nghiệm của phương trình $\sin x = -1$ là $x = -\frac{\pi}{2} + k\pi$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Đuôi phải là $+ k2\pi$, tức là $x = -\frac{\pi}{2} + k2\pi$. Vì trên đường tròn lượng giác chỉ có duy nhất 1 điểm dưới đáy có tung độ bằng $-1$!</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Phương trình $\sin x = \sin 30^\circ$ có nghiệm tính theo độ là $x = 30^\circ + k360^\circ$ và $x = 150^\circ + k360^\circ$ ($k \in \mathbb{Z}$). Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Khi dùng đơn vị độ, $180^\circ - 30^\circ = 150^\circ$ và đuôi là $k360^\circ$.</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Phương trình $\cos x = \cos\alpha$ có công thức nghiệm là $x = \alpha + k\pi$ và $x = -\alpha + k\pi$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Đuôi của cosin BẮT BUỘC là $k2\pi$ chứ không phải $k\pi$: $x = \pm\alpha + k2\pi$.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Phương trình lượng giác</div>
      <div class="quiz-q-text">Giải phương trình: $\sin 3x - \cos x = 0$. Nêu rõ bước chuyển vế và công thức phụ chéo được sử dụng.</div>
      <textarea placeholder="Trình bày bài giải của bạn vào đây..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Bước 1: Chuyển vế: $\sin 3x = \cos x$.
        <br>&bull; Bước 2: Dùng công thức phụ chéo biến cos thành sin: $\cos x = \sin(\frac{\pi}{2} - x)$.
        <br>&bull; Phương trình trở thành: $\sin 3x = \sin(\frac{\pi}{2} - x)$.
        <br>&bull; Họ 1: $3x = \frac{\pi}{2} - x + k2\pi \Leftrightarrow 4x = \frac{\pi}{2} + k2\pi \Rightarrow \mathbf{x = \frac{\pi}{8} + k\frac{\pi}{2}}$.
        <br>&bull; Họ 2: $3x = \pi - (\frac{\pi}{2} - x) + k2\pi = \frac{\pi}{2} + x + k2\pi \Leftrightarrow 2x = \frac{\pi}{2} + k2\pi \Rightarrow \mathbf{x = \frac{\pi}{4} + k\pi}$ ($k \in \mathbb{Z}$).
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Một viên đạn pháo được bắn từ mặt đất với vận tốc ban đầu $v_0 = 500\text{ m/s}$ nghiêng góc $\alpha$ so với phương ngang. Tầm xa đạt được là $L = \frac{v_0^2 \sin 2\alpha}{g}$ (với $g = 9,8\text{ m/s}^2$). Góc bắn $\alpha$ bằng bao nhiêu độ để tầm xa bắn xa nhất? Giải thích tại sao.</div>
      <textarea placeholder="Giải thích và tìm góc alpha..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Ta có $L = \frac{v_0^2}{g} \sin 2\alpha$.
        <br>&bull; Vì $\frac{v_0^2}{g}$ là hằng số dương và $\sin 2\alpha \le 1$, nên tầm xa $L$ lớn nhất khi và chỉ khi $\sin 2\alpha = 1$.
        <br>&bull; Giải phương trình: $2\alpha = 90^\circ + k360^\circ \Rightarrow \alpha = 45^\circ + k180^\circ$.
        <br>&bull; Do góc bắn thực tế $0^\circ < \alpha < 90^\circ$ nên ta chọn $\mathbf{\alpha = 45^\circ}$.
        <br>&bull; Kết luận: Bắn ở góc $45^\circ$ đạn pháo sẽ bay xa nhất!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b4')">🏆 Chấm Điểm Bài 4 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""
