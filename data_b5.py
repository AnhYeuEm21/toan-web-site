# -*- coding: utf-8 -*-
"""
data_b5.py - BÀI 5: DÃY SỐ (CHƯƠNG II ĐẠI SỐ 11)
SGK Kết Nối Tri Thức &bull; Trang 43 &ndash; 48
Kèm 15 câu trắc nghiệm kiểm tra độ hiểu bài.
"""

B5_CONTENT = r"""
<section class="lesson-section" id="bai-5">
  <div class="lesson-header">
    <div class="lesson-number">5</div>
    <div class="lesson-meta">
      <h2>BÀI 5: DÃY SỐ (CHƯƠNG II)</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương II &bull; Trang 43 &ndash; 48</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Dãy số vô hạn & hữu hạn</span>
        <span class="lesson-tag">Số hạng tổng quát</span>
        <span class="lesson-tag">Hệ thức truy hồi</span>
        <span class="lesson-tag">Dãy tăng & Dãy giảm</span>
        <span class="lesson-tag">Dãy số bị chặn</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('page_19.png')">📖 Xem SGK Trang 43-44</button>
    <button class="sgk-btn" onclick="openSgkModal('page_20.png')">📖 Xem SGK Trang 45-46</button>
    <button class="sgk-btn" onclick="openSgkModal('page_21.png')">📖 Xem SGK Trang 47-48</button>
  </div>

  <!-- PHẦN 1: ĐỊNH NGHĨA DÃY SỐ -->
  <h3 class="sec-title" id="b5-dinh-nghia">1. "Dịch" Dãy Số Sang Tiếng Người (Băm Nát Khái Niệm)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DÃY SỐ THỰC CHẤT LÀ CÁI GÌ?</div>
    <p>Sách giáo khoa ghi: <em>"Mỗi hàm số u xác định trên tập các số nguyên dương $\mathbb{N}^*$ được gọi là một dãy số vô hạn..."</em>. Nghe ghê gớm nhưng hiểu nôm na thế này:</p>
    <p style="margin-top:6px;">Dãy số giống như <strong>một hàng người xếp hàng vào rạp chiếu phim</strong>:</p>
    <ul class="content-list">
      <li>Người đứng ở vị trí số 1 gọi là số hạng đầu: <strong>$u_1$</strong>.</li>
      <li>Người đứng ở vị trí số 2 gọi là số hạng thứ hai: <strong>$u_2$</strong>.</li>
      <li>Người đứng ở vị trí số $n$ gọi là số hạng thứ $n$ (hay <strong>số hạng tổng quát $u_n$</strong>).</li>
      <li>Biến số $n$ <strong>BẮT BUỘC PHẢI LÀ SỐ NGUYÊN DƯƠNG</strong> ($n \in \{1, 2, 3, 4, ...\}$), không bao giờ có người đứng ở vị trí số $0$ hay vị trí số $-2,5$!</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BỐN CÁCH CHO MỘT DÃY SỐ TRONG ĐỀ THI</div>
    <div class="accordion-item">
      <button class="accordion-trigger open" onclick="toggleAcc(this)">
        <span>1. Cho bằng công thức số hạng tổng quát (Thích nhất!)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content open">
        <div class="accordion-inner">
          <p>Có công thức $u_n$ theo $n$, muốn tìm số hạng thứ bao nhiêu chỉ cần thay số $n$ vào là xong!</p>
          <p style="color:var(--accent-yellow);margin-top:4px;">Ví dụ: $u_n = 2n - 1$. Số hạng đầu $u_1 = 2(1) - 1 = 1$; Số hạng thứ 100 là $u_{100} = 2(100) - 1 = 199$.</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>2. Cho bằng hệ thức truy hồi (Kiểu "dây chuyền Domino")</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Cho biết số hạng đầu $u_1$, còn số hạng đứng sau $u_n$ được tính dựa vào số hạng đứng ngay trước nó $u_{n-1}$.</p>
          <p style="color:var(--accent-yellow);margin-top:4px;">Ví dụ: $\begin{cases} u_1 = 3 \\ u_n = u_{n-1} + 4 \end{cases} \Rightarrow u_2 = u_1 + 4 = 7 ; u_3 = u_2 + 4 = 11...$</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>3. Cho bằng cách liệt kê</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Liệt kê trực tiếp các số: $1, 3, 5, 7, 9, 11$ (chỉ dùng cho dãy hữu hạn ít số hạng).</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>4. Cho bằng phương pháp mô tả</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Dùng lời văn mô tả quy luật. Ví dụ: Dãy các số nguyên tố theo thứ tự tăng dần: $2, 3, 5, 7, 11, 13...$</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 2: DÃY SỐ TĂNG & DÃY SỐ GIẢM -->
  <h3 class="sec-title" id="b5-tang-giam">2. Dãy Số Tăng & Dãy Số Giảm (Cách Xét Chuẩn Điểm 10)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: THẾ NÀO LÀ TĂNG, THẾ NÀO LÀ GIẢM?</div>
    <ul class="content-list">
      <li><strong>Dãy số TĂNG:</strong> Số đứng sau luôn luôn LỚN HƠN số đứng trước: <strong>$u_{n+1} > u_n$</strong> (với mọi $n \ge 1$). Giống như leo cầu thang đi lên!</li>
      <li><strong>Dãy số GIẢM:</strong> Số đứng sau luôn luôn NHỎ HƠN số đứng trước: <strong>$u_{n+1} < u_n$</strong> (với mọi $n \ge 1$). Giống như tụt dốc cầu trượt!</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 HAI PHƯƠNG PHÁP XÉT TÍNH TĂNG - GIẢM BẤT HỦ</div>
    <p><strong>CÁCH 1: XÉT HIỆU $u_{n+1} - u_n$ (Dùng cho mọi bài toán dạng đa thức, phân thức)</strong></p>
    <div class="formula-display">
      &bull; Nếu u<sub>n+1</sub> &minus; u<sub>n</sub> &gt; 0   &rArr;   Dãy số TĂNG<br>
      &bull; Nếu u<sub>n+1</sub> &minus; u<sub>n</sub> &lt; 0   &rArr;   Dãy số GIẢM
    </div>
    <p style="margin-top:10px;"><strong>CÁCH 2: XÉT TỈ SỐ $\frac{u_{n+1}}{u_n}$ (CHỈ ĐƯỢC DÙNG KHI CÁC SỐ HẠNG $u_n > 0$, chuyên trị mũ lũy thừa $a^n$)</strong></p>
    <div class="formula-display">
      &bull; Nếu <span class="fraction"><span class="num">u<sub>n+1</sub></span><span class="den">u<sub>n</sub></span></span> &gt; 1   &rArr;   Dãy số TĂNG<br>
      &bull; Nếu <span class="fraction"><span class="num">u<sub>n+1</sub></span><span class="den">u<sub>n</sub></span></span> &lt; 1   &rArr;   Dãy số GIẢM
    </div>
  </div>

  <!-- PHẦN 3: DÃY SỐ BỊ CHẶN -->
  <h3 class="sec-title" id="b5-bi-chan">3. Dãy Số Bị Chặn (Có Trần & Có Đáy)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH HÌNH TƯỢNG: TRẦN NHÀ VÀ SÀN NHÀ</div>
    <p>Hãy tưởng tượng mày đứng trong một căn phòng:</p>
    <ul class="content-list">
      <li><strong>BỊ CHẶN TRÊN:</strong> Có một cái "trần nhà" số $M$ mà tất cả các số hạng trong dãy dù có cố leo cao đến mấy cũng không bao giờ vượt qua nổi: <strong>$u_n \le M$</strong> (với mọi $n$).</li>
      <li><strong>BỊ CHẶN DƯỚI:</strong> Có một cái "sàn nhà" số $m$ mà tất cả các số hạng không bao giờ tụt xuống sâu hơn nó: <strong>$u_n \ge m$</strong> (với mọi $n$).</li>
      <li><strong>BỊ CHẶN (TOÀN DIỆN):</strong> Vừa bị chặn trên vừa bị chặn dưới: <strong>$m \le u_n \le M$</strong>.</li>
    </ul>
    <div class="formula-display" style="margin-top:10px;font-size:0.95rem;">
      Ví dụ kinh điển: u<sub>n</sub> = <span class="fraction"><span class="num">1</span><span class="den">n</span></span> (n &isin; &Nopf;<sup>*</sup>)<br>
      Ta có: 0 &lt; <span class="fraction"><span class="num">1</span><span class="den">n</span></span> &le; 1   &rArr;   Dãy bị chặn dưới bởi 0, bị chặn trên bởi 1 &rArr; BỊ CHẶN!
    </div>
  </div>

  <!-- PHẦN 4: THỰC CHIẾN BÀI 5 -->
  <h3 class="sec-title" id="b5-thuc-chien">4. Thực Chiến Giải Bài Tập Mẫu Bài 5 (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP: XÉT TÍNH TĂNG, GIẢM CỦA DÃY SỐ PHÂN THỨC BẬC NHẤT</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Xét tính tăng, giảm của dãy số $(u_n)$ với $u_n = \frac{n}{n + 1}$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Viết công thức của số hạng kế tiếp $u_{n+1}$</strong>
          <p>Ở đâu có chữ $n$, ta thay bằng $(n + 1)$:</p>
          <p>$u_{n+1} = \frac{(n + 1)}{(n + 1) + 1} = \frac{n + 1}{n + 2}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Lập hiệu $u_{n+1} - u_n$ và quy đồng mẫu số</strong>
          <p>$u_{n+1} - u_n = \frac{n + 1}{n + 2} - \frac{n}{n + 1} = \frac{(n + 1)^2 - n(n + 2)}{(n + 2)(n + 1)}$.</p>
          <p>Khai triển tử số: $(n^2 + 2n + 1) - (n^2 + 2n) = \mathbf{1}$.</p>
          <p>Hiệu số trở thành: $u_{n+1} - u_n = \frac{1}{(n + 2)(n + 1)}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Đánh giá dấu và đưa ra kết luận</strong>
          <p>Vì $n \in \mathbb{N}^*$ ($n \ge 1$) nên mẫu số $(n + 2)(n + 1) > 0$.</p>
          <p>Tử số $1 > 0 \Rightarrow \mathbf{u_{n+1} - u_n > 0}$ với mọi $n \in \mathbb{N}^*$.</p>
          <p><strong>Kết luận:</strong> Dãy số $(u_n)$ là <strong>DÃY SỐ TĂNG</strong>!</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 5: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 5 -->
  <div class="quiz-section" id="b5-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 5 (15 CÂU)</div>
        <div class="quiz-sub">Dãy tăng giảm, dãy bị chặn, tìm số hạng &bull; Đạt 12/15 là xuất sắc!</div>
      </div>
      <div class="quiz-score-badge" id="b5-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho dãy số $(u_n)$ có số hạng tổng quát $u_n = 3n - 2$. Số hạng thứ 5 ($u_5$) của dãy số là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q1" value="A"> A. $11$</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="B"> B. $13$</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="C"> C. $15$</label>
        <label class="quiz-option"><input type="radio" name="b5_q1" value="D"> D. $17$</label>
      </div>
      <div class="quiz-explain">Giải thích: Thay $n = 5$ vào công thức: $u_5 = 3(5) - 2 = 15 - 2 = 13$. Chọn B.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Dãy số nào sau đây là DÃY SỐ TĂNG?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q2" value="A"> A. $u_n = 2n + 1$</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="B"> B. $u_n = -3n + 5$</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="C"> C. $u_n = \frac{1}{n}$</label>
        <label class="quiz-option"><input type="radio" name="b5_q2" value="D"> D. $u_n = (-1)^n$</label>
      </div>
      <div class="quiz-explain">Giải thích: Với $u_n = 2n + 1$, ta có $u_{n+1} - u_n = [2(n+1)+1] - (2n+1) = 2 > 0 \Rightarrow$ Dãy số tăng. Chọn A.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Dãy số $(u_n)$ với $u_n = \frac{1}{n^2 + 1}$ là dãy số:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q3" value="A"> A. Tăng</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="B"> B. Không tăng không giảm</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="C"> C. Giảm</label>
        <label class="quiz-option"><input type="radio" name="b5_q3" value="D"> D. Dãy hằng</label>
      </div>
      <div class="quiz-explain">Giải thích: Khi $n$ tăng dần thì mẫu số $n^2 + 1$ tăng dần, do đó phân số $\frac{1}{n^2 + 1}$ giảm dần $\Rightarrow$ Dãy số giảm. Chọn C.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Dãy số nào sau đây BỊ CHẶN DƯỚI bởi số 0 và BỊ CHẶN TRÊN bởi số 1?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q4" value="A"> A. $u_n = n$</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="B"> B. $u_n = 2^n$</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="C"> C. $u_n = -n^2$</label>
        <label class="quiz-option"><input type="radio" name="b5_q4" value="D"> D. $u_n = \frac{n}{n + 1}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Vì $n \ge 1$ nên $0 < \frac{n}{n+1} < 1$. Dãy vừa bị chặn dưới bởi 0, vừa bị chặn trên bởi 1. Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho dãy số $(u_n)$ xác định bởi hệ thức truy hồi: $u_1 = 2$ và $u_n = 2u_{n-1} + 1$ với $n \ge 2$. Số hạng $u_3$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q5" value="A"> A. $11$</label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="B"> B. $5$</label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="C"> C. $7$</label>
        <label class="quiz-option"><input type="radio" name="b5_q5" value="D"> D. $15$</label>
      </div>
      <div class="quiz-explain">Giải thích: $u_2 = 2u_1 + 1 = 2(2) + 1 = 5$. $u_3 = 2u_2 + 1 = 2(5) + 1 = 11$. Chọn A.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Dãy số $u_n = (-1)^n$ có tính chất nào sau đây?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q6" value="A"> A. Là dãy số tăng</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="B"> B. Là dãy số giảm</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="C"> C. Bị chặn trên bởi 1 và bị chặn dưới bởi &minus;1</label>
        <label class="quiz-option"><input type="radio" name="b5_q6" value="D"> D. Không bị chặn</label>
      </div>
      <div class="quiz-explain">Giải thích: Dãy đan dấu: $-1, 1, -1, 1...$ không tăng không giảm, nhưng $-1 \le u_n \le 1$ nên nó là dãy bị chặn. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Trong các dãy số sau, dãy số nào BỊ CHẶN DƯỚI nhưng KHÔNG BỊ CHẶN TRÊN?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q7" value="A"> A. $u_n = \sin n$</label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="B"> B. $u_n = n^2 + 2$</label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="C"> C. $u_n = -n$</label>
        <label class="quiz-option"><input type="radio" name="b5_q7" value="D"> D. $u_n = \frac{1}{n}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $n^2 + 2 \ge 1^2 + 2 = 3$ với mọi $n \ge 1$ (bị chặn dưới bởi 3). Khi $n \to +\infty$ thì $n^2+2 \to +\infty$ nên không bị chặn trên. Chọn B.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Năm số hạng đầu tiên của dãy số $u_n = \frac{n}{2^n}$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b5_q8" value="A"> A. $1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \frac{1}{16}$</label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="B"> B. $\frac{1}{2}, \frac{1}{2}, \frac{3}{8}, \frac{1}{4}, \frac{5}{16}$</label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="C"> C. $\frac{1}{2}, 1, \frac{3}{2}, 2, \frac{5}{2}$</label>
        <label class="quiz-option"><input type="radio" name="b5_q8" value="D"> D. $\frac{1}{2}, \frac{1}{2}, \frac{3}{8}, \frac{1}{4}, \frac{5}{32}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $u_1 = \frac{1}{2}$; $u_2 = \frac{2}{4} = \frac{1}{2}$; $u_3 = \frac{3}{8}$; $u_4 = \frac{4}{16} = \frac{1}{4}$; $u_5 = \frac{5}{32}$. Chọn D.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Tập xác định của mọi dãy số vô hạn $(u_n)$ luôn luôn là tập hợp các số nguyên dương $\mathbb{N}^* = \{1, 2, 3, ...\}$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Định nghĩa SGK: Dãy số vô hạn là hàm số có tập xác định là N*.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Mọi dãy số hoặc là dãy số tăng, hoặc là dãy số giảm. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Có những dãy số không tăng không giảm, ví dụ dãy đan dấu $u_n = (-1)^n$ hoặc dãy hằng $u_n = 5$ với mọi n.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu $u_{n+1} - u_n > 0$ với mọi $n \in \mathbb{N}^*$ thì dãy số $(u_n)$ là dãy số tăng. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! $u_{n+1} - u_n > 0 \Leftrightarrow u_{n+1} > u_n$, tức số sau lớn hơn số trước nên dãy tăng.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Dãy số $u_n = \cos n$ là một dãy số bị chặn. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Vì $-1 \le \cos n \le 1$ với mọi số nguyên dương $n$.</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Dãy số $u_n = 3n + 2$ là dãy số bị chặn trên. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Khi $n$ tăng vô hạn thì $3n + 2$ tăng vô hạn ra $+\infty$, không có số $M$ nào chặn được ở trên.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Dự đoán số hạng tổng quát</div>
      <div class="quiz-q-text">Cho dãy số $(u_n)$ được xác định bởi: $u_1 = 1$ và $u_n = n \times u_{n-1}$ với mọi $n \ge 2$. Hãy tính $u_2, u_3, u_4, u_5$ và dự đoán công thức số hạng tổng quát $u_n$ theo $n$.</div>
      <textarea placeholder="Ghi 5 số hạng đầu và công thức un..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; $u_1 = 1$.
        <br>&bull; $u_2 = 2 \times u_1 = 2 \times 1 = 2$.
        <br>&bull; $u_3 = 3 \times u_2 = 3 \times 2 \times 1 = 6$.
        <br>&bull; $u_4 = 4 \times u_3 = 4 \times 3 \times 2 \times 1 = 24$.
        <br>&bull; $u_5 = 5 \times u_4 = 120$.
        <br>&bull; Dự đoán công thức tổng quát: <strong>$u_n = n!$ (n giai thừa: $1 \times 2 \times 3 \times ... \times n$)</strong>.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Dân số của một thành phố năm 2020 là 500 nghìn người, tăng trưởng 2% mỗi năm. Công thức dân số sau $n$ năm là $P_n = 500(1 + 0,02)^n$. Hỏi vào năm 2030, dân số thành phố ước tính khoảng bao nhiêu nghìn người? (Làm tròn đến hàng đơn vị).</div>
      <textarea placeholder="Nhập số năm n và kết quả dân số..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Từ năm 2020 đến 2030 có số năm là: $n = 2030 - 2020 = 10$ năm.
        <br>&bull; Thay $n = 10$ vào công thức: $P_{10} = 500 \times (1 + 0,02)^{10} = 500 \times (1,02)^{10} \approx 500 \times 1,218994 = \mathbf{609\text{ nghìn người}}$.
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b5')">🏆 Chấm Điểm Bài 5 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""
