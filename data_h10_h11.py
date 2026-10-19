# -*- coding: utf-8 -*-
"""
data_h10_h11.py - BÀI 10 & BÀI 11 (CHƯƠNG IV HÌNH HỌC KHÔNG GIAN 11)
Bao gồm:
- Bài 10: Đường thẳng và mặt phẳng trong không gian (SGK trang 70 - 77)
- Bài 11: Hai đường thẳng song song (SGK trang 78 - 83)
Kèm 15 câu trắc nghiệm kiểm tra độ hiểu bài cho từng bài.
"""

H10_CONTENT = r"""
<section class="lesson-section" id="bai-10">
  <div class="lesson-header">
    <div class="lesson-number">10</div>
    <div class="lesson-meta">
      <h2>BÀI 10: ĐƯỜNG THẲNG VÀ MẶT PHẲNG TRONG KHÔNG GIAN</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương IV &bull; Trang 70 &ndash; 77</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Mặt phẳng không gian</span>
        <span class="lesson-tag">Quy tắc nét liền & nét đứt</span>
        <span class="lesson-tag">Tìm giao tuyến 2 mặt phẳng</span>
        <span class="lesson-tag">Tìm giao điểm đường & mặt</span>
        <span class="lesson-tag">Hình chóp & Tứ diện</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('hinh_01.png')">📖 Xem SGK Trang 70-71</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_02.png')">📖 Xem SGK Trang 72-73</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_03.png')">📖 Xem SGK Trang 74-75</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_04.png')">📖 Xem SGK Trang 76-77</button>
  </div>

  <!-- PHẦN 1: MẶT PHẲNG LÀ GÌ -->
  <h3 class="sec-title" id="h10-mat-phang">1. "Dịch" Mặt Phẳng Sang Tiếng Người (Chống Lú Hình Học)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: MẶT PHẲNG KHÔNG PHẢI LÀ CÁI MẶT BÀN!</div>
    <p>Nhiều đứa mất gốc nhìn hình vẽ trong vở (vẽ hình bình hành có chữ $P$ ở góc) lại ngây thơ nghĩ: <em>"Mặt phẳng là cái hình bình hành có 4 góc cạnh giới hạn"</em>. <strong>SAI HOÀN TOÀN!</strong></p>
    <p style="margin-top:6px;">Hiểu đúng bản chất:</p>
    <ul class="content-list">
      <li><strong>Mặt phẳng:</strong> Giống như <strong>mặt nước hồ phẳng lặng trải dài vô tận</strong> về bốn phương tám hướng không có bờ bến, và <strong>hoàn toàn không có bề dày</strong> (độ dày bằng 0).</li>
      <li>Cái hình bình hành ta vẽ trong vở chỉ là <em>một góc biểu diễn tượng trưng</em> mà thôi. Đừng bao giờ nghĩ nó bị chặn lại ở mép hình!</li>
      <li>Kí hiệu mặt phẳng: Đặt tên bằng chữ in hoa hoặc chữ Hy Lạp trong ngoặc đơn: mặt phẳng $(P)$, $(Q)$, mặt phẳng $(\alpha)$, $(\beta)$, hoặc $(ABC)$ (mặt phẳng đi qua 3 điểm $A, B, C$).</li>
    </ul>
  </div>

  <div class="box box-warning">
    <div class="box-title">⚠️ QUY TẮC VẼ HÌNH KHÔNG GIAN BẮT BUỘC (VẼ SAI LÀ ĂN 0 ĐIỂM)</div>
    <ul class="content-list">
      <li><strong>Nét nhìn thấy:</strong> Phải vẽ bằng <strong>NÉT LIỀN (____)</strong>.</li>
      <li><strong>Nét bị che khuất (nằm khuất bên trong hoặc phía sau):</strong> BẮT BUỘC phải vẽ bằng <strong>NÉT ĐỨT (- - - -)</strong>.</li>
      <li>Hai đường thẳng song song ngoài đời $\Rightarrow$ Vào hình vẽ BẮT BUỘC phải vẽ <strong>SONG SONG</strong>.</li>
      <li>Tỉ số đoạn thẳng trên cùng một đường thẳng được giữ nguyên (ví dụ trung điểm thì vào hình vẽ vẫn phải lấy đúng chính giữa).</li>
      <li>Nhưng <strong>góc vuông ngoài đời vào hình không gian KHÔNG CẦN VUÔNG</strong>! Tam giác vuông, tam giác đều, tam giác cân vào hình biểu diễn đều được vẽ thành tam giác thường, chỉ cần đánh dấu góc vuông vào là xong!</li>
    </ul>
  </div>

  <!-- PHẦN 2: CÁC TÍNH CHẤT THỪA NHẬN VÀ XÁC ĐỊNH MẶT PHẲNG -->
  <h3 class="sec-title" id="h10-tinh-chat">2. Ba Cách Xác Định Mặt Phẳng (Kê Bàn Không Bị Bập Bênh)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 VÍ DỤ ĐỜI THƯỜNG: TẠI SAO GHẾ 3 CHÂN KHÔNG BAO GIỜ BẬP BÊNH?</div>
    <p>Mày đi uống trà chanh thấy ghế 4 chân hay bị kênh, phải lót bìa các-tông dưới chân? Nhưng cái kiềng 3 chân đun bếp hay cái giá đỡ máy ảnh 3 chân đặt đâu cũng đứng vững như bàn thạch!</p>
    <p style="margin-top:6px;">Lý do toán học: <strong>Qua 3 điểm không thẳng hàng, luôn luôn xác định DUY NHẤT một mặt phẳng!</strong></p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BA CÁCH TẠO RA MỘT MẶT PHẲNG DUY NHẤT TRONG KHÔNG GIAN</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px;">
      <div style="background:var(--bg-secondary);padding:12px;border-radius:var(--radius-sm);">
        <strong style="color:var(--accent-blue-light);">Cách 1: Qua 3 điểm</strong>
        <p style="font-size:0.85rem;margin-top:6px;">Ba điểm $A, B, C$ không thẳng hàng xác định duy nhất mặt phẳng $(ABC)$.</p>
      </div>
      <div style="background:var(--bg-secondary);padding:12px;border-radius:var(--radius-sm);">
        <strong style="color:var(--accent-yellow);">Cách 2: 1 điểm + 1 đường thẳng</strong>
        <p style="font-size:0.85rem;margin-top:6px;">Một đường thẳng $d$ và một điểm $A$ nằm ngoài $d$ xác định duy nhất mặt phẳng $(A, d)$.</p>
      </div>
      <div style="background:var(--bg-secondary);padding:12px;border-radius:var(--radius-sm);">
        <strong style="color:var(--accent-green);">Cách 3: 2 đường thẳng cắt nhau</strong>
        <p style="font-size:0.85rem;margin-top:6px;">Hai đường thẳng $a$ và $b$ cắt nhau tại điểm $O$ xác định duy nhất mặt phẳng $(a, b)$.</p>
      </div>
    </div>
  </div>

  <!-- PHẦN 3: HÌNH CHÓP VÀ TỨ DIỆN -->
  <h3 class="sec-title" id="h10-chop-tu-dien">3. Hình Chóp & Hình Tứ Diện (Nhân Vật Chính Của Mọi Đề Thi)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 PHÂN BIỆT HÌNH CHÓP VÀ HÌNH TỨ DIỆN</div>
    <ul class="content-list">
      <li><strong>Hình chóp $S.A_1 A_2 ... A_n$:</strong>
        <br>&bull; Đỉnh là điểm $S$ nằm lơ lửng trên cao.
        <br>&bull; Đáy là một đa giác nằm dưới sàn: đáy tam giác (chóp tam giác), đáy tứ giác (chóp tứ giác $S.ABCD$).
        <br>&bull; Các mặt bên là các hình tam giác có chung đỉnh $S$.
      </li>
      <li><strong>Hình tứ diện $ABCD$ (Chóp tam giác):</strong>
        <br>&bull; "Tứ" là 4, "diện" là mặt. Khối đa diện có đúng <strong>4 mặt đều là các hình tam giác</strong>.
        <br>&bull; Điểm đặc biệt: Bất kì đỉnh nào cũng có thể đóng vai trò là ĐỈNH, và mặt đối diện đóng vai trò là ĐÁY!
        <br>&bull; Hai cạnh không có điểm chung gọi là <strong>hai cạnh đối diện</strong> (ví dụ: $AB$ đối diện $CD$, $AC$ đối diện $BD$, $AD$ đối diện $BC$).
      </li>
    </ul>
  </div>

  <!-- PHẦN 4: HAI KỸ NĂNG VÀNG THI GIỮA KÌ -->
  <h3 class="sec-title" id="h10-ky-nang-vang">4. Hai Kỹ Năng Sống Còn: Tìm Giao Tuyến & Tìm Giao Điểm</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 KỸ NĂNG 1: TÌM GIAO TUYẾN CỦA HAI MẶT PHẲNG (P) VÀ (Q)</div>
    <div class="step-solver-body">
      <p><strong>Bản chất giao tuyến:</strong> Giao tuyến là đường thẳng chung duy nhất đi qua tất cả các điểm chung của 2 mặt phẳng.</p>
      <div class="formula-display" style="font-size:0.95rem;">
        Muốn tìm giao tuyến &rArr; BẮT BUỘC PHẢI TÌM ĐƯỢC 2 ĐIỂM CHUNG PHÂN BIỆT!
      </div>
      <div class="step" style="margin-top:10px;">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Điểm chung thứ nhất:</strong> Thường là điểm dễ nhìn thấy ngay trên tên gọi của 2 mặt phẳng (ví dụ: tìm giao tuyến của $(SAC)$ và $(SBD)$ thì điểm chung thứ nhất chính là đỉnh $S$).
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Điểm chung thứ hai:</strong> Tìm trong mặt phẳng $(P)$ một đường thẳng $a$, trong mặt phẳng $(Q)$ một đường thẳng $b$ sao cho $a$ và $b$ <em>CÙNG NẰM TRONG MỘT MẶT PHẲNG THỨ BA</em> (thường là mặt đáy). Cho $a$ cắt $b$ tại điểm $I$. Điểm $I$ chính là điểm chung thứ hai!
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Kết luận:</strong> Nối 2 điểm chung lại: đường thẳng $SI$ chính là giao tuyến cần tìm!
        </div>
      </div>
    </div>
  </div>

  <div class="step-solver">
    <div class="step-solver-header">🎯 KỸ NĂNG 2: TÌM GIAO ĐIỂM CỦA ĐƯỜNG THẲNG d VỚI MẶT PHẲNG (&alpha;)</div>
    <div class="step-solver-body">
      <p>Nhiều đứa cứ lấy bút kéo dài đường thẳng $d$ lung tung rồi cho cắt bừa một đường trong mặt phẳng $(\alpha)$. <strong>SAI NGU!</strong> Trong không gian, hai đường muốn cắt nhau thì BẮT BUỘC chúng phải cùng nằm trong một mặt phẳng!</p>
      <p><strong>Quy trình 3 bước chuẩn SGK:</strong></p>
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1:</strong> Chọn một mặt phẳng phụ $(\beta)$ chứa đường thẳng $d$ (chọn mặt nào dễ tìm giao tuyến nhất).
        </div>
      </div>
      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2:</strong> Tìm giao tuyến $a = (\beta) \cap (\alpha)$.
        </div>
      </div>
      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3:</strong> Trong mặt phẳng phụ $(\beta)$, cho đường thẳng $d$ cắt giao tuyến $a$ tại điểm $M$. Điểm $M$ chính là giao điểm của $d$ với mặt phẳng $(\alpha)$!
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 5: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 10 -->
  <div class="quiz-section" id="b10-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 10 (15 CÂU)</div>
        <div class="quiz-sub">Điểm thuộc mặt phẳng, xác định mặt phẳng, tìm giao tuyến & giao điểm &bull; Đạt 12/15 là đỗ!</div>
      </div>
      <div class="quiz-score-badge" id="b10-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Trong không gian, có bao nhiêu mặt phẳng đi qua ba điểm không thẳng hàng?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q1" value="A"> A. Duy nhất 1</label>
        <label class="quiz-option"><input type="radio" name="b10_q1" value="B"> B. 2</label>
        <label class="quiz-option"><input type="radio" name="b10_q1" value="C"> C. Vô số</label>
        <label class="quiz-option"><input type="radio" name="b10_q1" value="D"> D. 3</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất thừa nhận 2: Có một và chỉ một mặt phẳng đi qua ba điểm không thẳng hàng. Chọn A.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Một hình chóp tứ giác $S.ABCD$ có bao nhiêu cạnh?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q2" value="A"> A. 4</label>
        <label class="quiz-option"><input type="radio" name="b10_q2" value="B"> B. 6</label>
        <label class="quiz-option"><input type="radio" name="b10_q2" value="C"> C. 8</label>
        <label class="quiz-option"><input type="radio" name="b10_q2" value="D"> D. 5</label>
      </div>
      <div class="quiz-explain">Giải thích: Gồm 4 cạnh đáy (AB, BC, CD, DA) và 4 cạnh bên (SA, SB, SC, SD), tổng cộng có 8 cạnh. Chọn C.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hình tứ diện có bao nhiêu mặt và bao nhiêu đỉnh?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q3" value="A"> A. 3 mặt, 4 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b10_q3" value="B"> B. 4 mặt, 4 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b10_q3" value="C"> C. 4 mặt, 6 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b10_q3" value="D"> D. 5 mặt, 5 đỉnh</label>
      </div>
      <div class="quiz-explain">Giải thích: Tứ diện ABCD có 4 mặt (ABC, ABD, ACD, BCD), 4 đỉnh (A, B, C, D) và 6 cạnh. Chọn B.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nếu hai mặt phẳng phân biệt có một điểm chung thì chúng có:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q4" value="A"> A. Duy nhất điểm chung đó</label>
        <label class="quiz-option"><input type="radio" name="b10_q4" value="B"> B. 2 điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b10_q4" value="C"> C. Vô số đường thẳng chung</label>
        <label class="quiz-option"><input type="radio" name="b10_q4" value="D"> D. Một đường thẳng chung duy nhất đi qua điểm đó</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất thừa nhận 4: Nếu hai mặt phẳng phân biệt có một điểm chung thì chúng có một đường thẳng chung duy nhất chứa tất cả các điểm chung của hai mặt phẳng đó (đường thẳng này gọi là giao tuyến). Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Giao tuyến của hai mặt phẳng $(SAC)$ và $(SBD)$ là đường thẳng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q5" value="A"> A. $SO$</label>
        <label class="quiz-option"><input type="radio" name="b10_q5" value="B"> B. $SA$</label>
        <label class="quiz-option"><input type="radio" name="b10_q5" value="C"> C. $AC$</label>
        <label class="quiz-option"><input type="radio" name="b10_q5" value="D"> D. $SD$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hai mặt phẳng có điểm chung thứ nhất là $S$. Dưới đáy $ABCD$, $AC \cap BD = O \Rightarrow O$ là điểm chung thứ hai. Giao tuyến là đường thẳng nối 2 điểm chung: $SO$. Chọn A.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Quy tắc biểu diễn nào sau đây là SAI khi vẽ hình học không gian?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q6" value="A"> A. Đường nhìn thấy vẽ nét liền</label>
        <label class="quiz-option"><input type="radio" name="b10_q6" value="B"> B. Đường bị che khuất vẽ nét đứt</label>
        <label class="quiz-option"><input type="radio" name="b10_q6" value="C"> C. Tam giác vuông bắt buộc phải vẽ thành tam giác có một góc vuông $90^\circ$</label>
        <label class="quiz-option"><input type="radio" name="b10_q6" value="D"> D. Hai đường thẳng song song phải vẽ thành hai đường thẳng song song</label>
      </div>
      <div class="quiz-explain">Giải thích: Trong hình học không gian, tam giác vuông, đều hay cân đều được biểu diễn bằng tam giác thường tùy góc nhìn, không bắt buộc phải vẽ góc $90^\circ$. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho tứ diện $ABCD$. Cặp cạnh nào sau đây là hai cạnh đối diện nhau?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q7" value="A"> A. $AB$ và $BC$</label>
        <label class="quiz-option"><input type="radio" name="b10_q7" value="B"> B. $AB$ và $CD$</label>
        <label class="quiz-option"><input type="radio" name="b10_q7" value="C"> C. $AC$ và $AD$</label>
        <label class="quiz-option"><input type="radio" name="b10_q7" value="D"> D. $BC$ và $CD$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hai cạnh đối diện trong tứ diện là hai cạnh không có đỉnh chung: $AB$ đối diện $CD$, $AC$ đối diện $BD$, $AD$ đối diện $BC$. Chọn B.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho 4 điểm $A, B, C, D$ không cùng thuộc một mặt phẳng. Số mặt phẳng được tạo bởi 3 trong 4 điểm này là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b10_q8" value="A"> A. 4 mặt phẳng</label>
        <label class="quiz-option"><input type="radio" name="b10_q8" value="B"> B. 6 mặt phẳng</label>
        <label class="quiz-option"><input type="radio" name="b10_q8" value="C"> C. 3 mặt phẳng</label>
        <label class="quiz-option"><input type="radio" name="b10_q8" value="D"> D. Vô số mặt phẳng</label>
      </div>
      <div class="quiz-explain">Giải thích: Số mặt phẳng tạo thành chính là 4 mặt của hình tứ diện: $(ABC), (ABD), (ACD), (BCD)$. Chọn A.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu một đường thẳng có hai điểm phân biệt thuộc một mặt phẳng thì mọi điểm của đường thẳng đó đều thuộc mặt phẳng. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tính chất thừa nhận 3: Khi đường thẳng có 2 điểm nằm trong mặt phẳng thì toàn bộ đường thẳng nằm trọn trong mặt phẳng đó.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Mặt phẳng trong không gian bị giới hạn bởi một hình bình hành có bốn cạnh. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI BÉT! Mặt phẳng không có bề dày và mở rộng vô tận về mọi phía, không bị giới hạn bởi bất kì đường biên nào.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Một đường thẳng và một điểm không thuộc đường thẳng đó luôn xác định duy nhất một mặt phẳng. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Lấy 2 điểm phân biệt trên đường thẳng kết hợp với điểm ngoài đường thẳng tạo thành 3 điểm không thẳng hàng $\Rightarrow$ Xác định duy nhất 1 mặt phẳng.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hai đường thẳng bất kì trong không gian luôn luôn cắt nhau hoặc song song với nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Trong không gian còn có trường hợp kinh điển là HAI ĐƯỜNG THẲNG CHÉO NHAU (không cắt nhau và không cùng nằm trên mặt phẳng nào).</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Trong hình chóp tứ giác $S.ABCD$, hai đường chéo đáy $AC$ và $BD$ cắt nhau tại $O$ thì điểm $O$ thuộc cả hai mặt phẳng $(SAC)$ và $(SBD)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! $O \in AC \subset (SAC) \Rightarrow O \in (SAC)$. $O \in BD \subset (SBD) \Rightarrow O \in (SBD)$. $O$ là điểm chung của hai mặt phẳng.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Tìm giao tuyến</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang (hai đáy là $AB$ và $CD$, $AB > CD$). Hai cạnh bên của đáy $AD$ và $BC$ cắt nhau tại điểm $K$. Hãy tìm giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$.</div>
      <textarea placeholder="Trình bày các bước tìm 2 điểm chung..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Điểm chung thứ nhất: Rõ ràng đỉnh $S \in (SAD) \cap (SBC)$.
        <br>&bull; Điểm chung thứ hai: Trong mặt phẳng đáy $(ABCD)$, ta có $AD \cap BC = K$.
        <br>&bull; Vì $K \in AD \subset (SAD)$ nên $K \in (SAD)$.
        <br>&bull; Vì $K \in BC \subset (SBC)$ nên $K \in (SBC)$.
        <br>&bull; Vậy $K$ là điểm chung thứ hai.
        <br>&bull; Kết luận: <strong>Giao tuyến của $(SAD)$ và $(SBC)$ là đường thẳng $SK$</strong>.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Giải thích thực tế</div>
      <div class="quiz-q-text">Tại sao một chiếc bàn 4 chân khi đặt trên sàn nhà mấp mô thì hay bị bập bênh, trong khi chiếc bàn 3 chân thì luôn đứng vững không bao giờ bập bênh? Giải thích bằng nguyên lý hình học không gian.</div>
      <textarea placeholder="Giải thích dựa trên cách xác định mặt phẳng..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn ngôn ngữ khoa học đời thường:</strong>
        <br>&bull; Với bàn 3 chân: Ba đầu mút của 3 chân bàn luôn tạo thành 3 điểm không thẳng hàng. Qua 3 điểm không thẳng hàng LUÔN XÁC ĐỊNH DUY NHẤT MỘT MẶT PHẲNG. Do đó 3 chân bàn luôn cùng nằm trên một mặt phẳng phẳng phiu, không bao giờ bị bập bênh!
        <br>&bull; Với bàn 4 chân: Bốn đầu mút của 4 chân bàn là 4 điểm trong không gian. Nếu sàn nhà mấp mô, 4 điểm này nói chung KHÔNG ĐỒNG PHẲNG (không cùng nằm trên 1 mặt phẳng). Lúc này chỉ có 3 chân chạm đất còn chân thứ 4 bị hẫng lơ lửng trên không, gây ra hiện tượng bập bênh!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b10')">🏆 Chấm Điểm Bài 10 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""

H11_CONTENT = r"""
<section class="lesson-section" id="bai-11">
  <div class="lesson-header">
    <div class="lesson-number">11</div>
    <div class="lesson-meta">
      <h2>BÀI 11: HAI ĐƯỜNG THẲNG SONG SONG</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương IV &bull; Trang 78 &ndash; 83</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Hai đường thẳng chéo nhau</span>
        <span class="lesson-tag">Hai đường thẳng song song</span>
        <span class="lesson-tag">Định lý 3 giao tuyến song song</span>
        <span class="lesson-tag">Giao tuyến đi qua đỉnh song song đáy</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('hinh_05.png')">📖 Xem SGK Trang 78-79</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_06.png')">📖 Xem SGK Trang 80-81</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_07.png')">📖 Xem SGK Trang 82-83</button>
  </div>

  <!-- PHẦN 1: BỐN VỊ TRÍ TƯƠNG ĐỐI TRONG KHÔNG GIAN -->
  <h3 class="sec-title" id="h11-vi-tri-tuong-doi">1. Bốn Vị Trí Tương Đối Của Hai Đường Thẳng (Mổ Xẻ Tận Gốc)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: "CHÉO NHAU" LÀ GÌ?</div>
    <p>Hồi cấp 2 trong mặt phẳng, hai đường thẳng chỉ có 3 cửa: Cắt nhau, Song song hoặc Trùng nhau. Nhưng lên lớp 11 trong không gian 3 chiều, có một trường hợp quái vật xuất hiện: <strong>HAI ĐƯỜNG THẲNG CHÉO NHAU</strong>!</p>
    <ul class="content-list">
      <li><strong>Trường hợp 1: CÙNG NẰM TRONG MỘT MẶT PHẲNG (Đồng phẳng):</strong>
        <br>&bull; <em>Cắt nhau:</em> Có đúng 1 điểm chung duy nhất.
        <br>&bull; <em>Song song:</em> Cùng nằm trong 1 mặt phẳng và KHÔNG CÓ ĐIỂM CHUNG NÀO.
        <br>&bull; <em>Trùng nhau:</em> Có vô số điểm chung.
      </li>
      <li><strong>Trường hợp 2: KHÔNG CÙNG NẰM TRONG BẤT KÌ MẶT PHẲNG NÀO:</strong>
        <br>&bull; <strong>HAI ĐƯỜNG THẲNG CHÉO NHAU!</strong> Chúng không cắt nhau, cũng không song song với nhau.
      </li>
    </ul>
  </div>

  <div class="box box-story">
    <div class="box-title">✈️ VÍ DỤ ĐỜI THƯỜNG: MÁY BAY VÀ TÀU HỎA</div>
    <p>Hãy nhìn một chiếc máy bay đang bay trên bầu trời theo hướng Bắc &ndash; Nam ở độ cao $10.000\text{ m}$, và một đoàn tàu hỏa chạy trên mặt đất theo hướng Đông &ndash; Tây.</p>
    <p style="margin-top:6px;">Quỹ đạo bay của máy bay và đường ray tàu hỏa <strong>hoàn toàn không cắt nhau</strong> (không bao giờ đâm vào nhau), nhưng chúng cũng <strong>không hề song song</strong>! Đó chính là hình ảnh chân thực nhất của <strong>HAI ĐƯỜNG THẲNG CHÉO NHAU</strong> trong không gian!</p>
  </div>

  <!-- PHẦN 2: TÍNH CHẤT VÀ ĐỊNH LÝ GIAO TUYẾN SONG SONG -->
  <h3 class="sec-title" id="h11-dinh-ly-giao-tuyen">2. Định Lý Giao Tuyến Song Song (Vũ Khí Lấy Điểm 9 Giữa Kì)</h3>

  <div class="box box-formula">
    <div class="box-title">📐 ĐỊNH LÝ 1: TÍNH CHẤT BẮC CẦU CỦA ĐƯỜNG THẲNG SONG SONG</div>
    <div class="formula-display">
      Nếu a &parallel; c  và  b &parallel; c   &rArr;   a &parallel; b
    </div>
    <div class="formula-label">Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau</div>
  </div>

  <div class="box box-formula">
    <div class="box-title">🔥 ĐỊNH LÝ 2: ĐỊNH LÝ GIAO TUYẾN SONG SONG (CỰC KÌ HAY THI)</div>
    <div class="formula-display">
      <span style="display:inline-block;vertical-align:middle;text-align:left;">
        &bull; Mặt phẳng (&alpha;) chứa đường thẳng a<br>
        &bull; Mặt phẳng (&beta;) chứa đường thẳng b<br>
        &bull; Mà a &parallel; b<br>
        &bull; (&alpha;) c&abreve;t (&beta;) theo giao tuyến d
      </span>
      &nbsp;&nbsp;&rArr;&nbsp;&nbsp;
      <strong style="color:var(--accent-green);font-size:1.15rem;">Giao tuyến d &parallel; a &parallel; b</strong>
    </div>
    <div class="formula-label">Thần chú nhớ: "Hai mặt phẳng chứa hai đường song song thì giao tuyến của chúng PHẢI SONG SONG với hai đường đó!"</div>
  </div>

  <!-- PHẦN 3: DẠNG TOÁN THỰC CHIẾN KINH ĐIỂN -->
  <h3 class="sec-title" id="h11-thuc-chien">3. Dạng Toán Kinh Điển: Tìm Giao Tuyến Đi Qua Đỉnh & Song Song Đáy</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP: TÌM GIAO TUYẾN CỦA HAI MẶT BÊN CHỨA HAI CẠNH ĐÁY SONG SONG</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Tìm giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi điểm chung và hai đường thẳng song song</strong>
          <p>&bull; Nhìn vào tên hai mặt phẳng $(SAB)$ và $(SCD)$: Điểm chung thứ nhất là <strong>đỉnh $S$</strong>.</p>
          <p>&bull; Trong mặt phẳng $(SAB)$ có chứa đường thẳng $AB$.</p>
          <p>&bull; Trong mặt phẳng $(SCD)$ có chứa đường thẳng $CD$.</p>
          <p>&bull; Đáy $ABCD$ là hình bình hành nên <strong>$AB \parallel CD$</strong>!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Ốp định lý giao tuyến song song</strong>
          <p>Hai mặt phẳng $(SAB)$ và $(SCD)$ có điểm chung $S$ và lần lượt chứa hai đường thẳng song song $AB \parallel CD$.</p>
          <p>Theo định lý giao tuyến song song: <strong>Giao tuyến của chúng là đường thẳng $Sx$ đi qua điểm $S$ và song song với cả $AB$ và $CD$!</strong></p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Trình bày bài thi chuẩn mực không bị trừ một phần tư điểm</strong>
          <p>Ta có: $S \in (SAB) \cap (SCD)$.</p>
          <p>$\begin{cases} AB \subset (SAB) \\ CD \subset (SCD) \\ AB \parallel CD \end{cases} \Rightarrow (SAB) \cap (SCD) = Sx$ với $Sx \parallel AB \parallel CD$. Xong bài mẫu mực 10 điểm!</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 4: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 11 -->
  <div class="quiz-section" id="b11-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 11 (15 CÂU)</div>
        <div class="quiz-sub">Hai đường chéo nhau, định lý giao tuyến song song &bull; Đạt 12/15 là nắm chắc gốc!</div>
      </div>
      <div class="quiz-score-badge" id="b11-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hai đường thẳng được gọi là CHÉO NHAU nếu:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q1" value="A"> A. Chúng không có điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b11_q1" value="B"> B. Chúng nằm trong cùng một mặt phẳng và không cắt nhau</label>
        <label class="quiz-option"><input type="radio" name="b11_q1" value="C"> C. Chúng không cùng thuộc bất kì mặt phẳng nào</label>
        <label class="quiz-option"><input type="radio" name="b11_q1" value="D"> D. Chúng vuông góc với nhau</label>
      </div>
      <div class="quiz-explain">Giải thích: Định nghĩa SGK trang 79: Hai đường thẳng chéo nhau là hai đường thẳng không cùng nằm trong bất kì mặt phẳng nào. Chọn C.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Trong hình tứ diện $ABCD$, có bao nhiêu cặp đường thẳng chéo nhau?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q2" value="A"> A. 2 cặp</label>
        <label class="quiz-option"><input type="radio" name="b11_q2" value="B"> B. 3 cặp</label>
        <label class="quiz-option"><input type="radio" name="b11_q2" value="C"> C. 4 cặp</label>
        <label class="quiz-option"><input type="radio" name="b11_q2" value="D"> D. 6 cặp</label>
      </div>
      <div class="quiz-explain">Giải thích: Có đúng 3 cặp cạnh đối diện là 3 cặp đường thẳng chéo nhau: (AB và CD), (AC và BD), (AD và BC). Chọn B.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang ($AB \parallel CD$). Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q3" value="A"> A. Đường thẳng đi qua $S$ và song song với $AB, CD$</label>
        <label class="quiz-option"><input type="radio" name="b11_q3" value="B"> B. Đường thẳng $SO$ với $O = AC \cap BD$</label>
        <label class="quiz-option"><input type="radio" name="b11_q3" value="C"> C. Đường thẳng $AB$</label>
        <label class="quiz-option"><input type="radio" name="b11_q3" value="D"> D. Hai mặt phẳng này không có giao tuyến</label>
      </div>
      <div class="quiz-explain">Giải thích: Theo định lý giao tuyến song song: Hai mặt phẳng có điểm chung S và lần lượt chứa 2 đường thẳng song song AB và CD thì giao tuyến phải đi qua S và song song với AB, CD. Chọn A.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho ba đường thẳng $a, b, c$ phân biệt trong không gian. Biết $a \parallel b$ và $b \parallel c$. Mối quan hệ giữa $a$ và $c$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q4" value="A"> A. $a$ chéo nhau với $c$</label>
        <label class="quiz-option"><input type="radio" name="b11_q4" value="B"> B. $a$ cắt $c$</label>
        <label class="quiz-option"><input type="radio" name="b11_q4" value="C"> C. $a$ trùng $c$</label>
        <label class="quiz-option"><input type="radio" name="b11_q4" value="D"> D. $a \parallel c$</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất bắc cầu: Hai đường thẳng phân biệt cùng song song với đường thẳng thứ ba thì song song với nhau ($a \parallel c$). Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $M, N$ lần lượt là trung điểm của $SA, SB$. Khẳng định nào sau đây là ĐÚNG?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q5" value="A"> A. $MN$ cắt $CD$</label>
        <label class="quiz-option"><input type="radio" name="b11_q5" value="B"> B. $MN \parallel CD$</label>
        <label class="quiz-option"><input type="radio" name="b11_q5" value="C"> C. $MN$ chéo nhau với $CD$</label>
        <label class="quiz-option"><input type="radio" name="b11_q5" value="D"> D. $MN \parallel SC$</label>
      </div>
      <div class="quiz-explain">Giải thích: $M, N$ là trung điểm của $SA, SB$ nên $MN$ là đường trung bình trong tam giác $SAB \Rightarrow MN \parallel AB$. Mặt khác $ABCD$ là hình bình hành nên $AB \parallel CD$. Theo tính chất bắc cầu: $MN \parallel CD$. Chọn B.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hai đường thẳng chéo nhau $a$ và $b$. Có bao nhiêu mặt phẳng chứa cả $a$ và $b$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q6" value="A"> A. Duy nhất 1</label>
        <label class="quiz-option"><input type="radio" name="b11_q6" value="B"> B. Vô số</label>
        <label class="quiz-option"><input type="radio" name="b11_q6" value="C"> C. Không có mặt phẳng nào ($0$ mặt phẳng)</label>
        <label class="quiz-option"><input type="radio" name="b11_q6" value="D"> D. 2 mặt phẳng</label>
      </div>
      <div class="quiz-explain">Giải thích: Định nghĩa hai đường thẳng chéo nhau là hai đường thẳng không cùng thuộc bất kì mặt phẳng nào, do đó không tồn tại mặt phẳng chứa cả hai đường này. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Qua một điểm $M$ nằm ngoài đường thẳng $d$, có bao nhiêu đường thẳng song song với $d$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q7" value="A"> A. Duy nhất 1</label>
        <label class="quiz-option"><input type="radio" name="b11_q7" value="B"> B. 2</label>
        <label class="quiz-option"><input type="radio" name="b11_q7" value="C"> C. Vô số</label>
        <label class="quiz-option"><input type="radio" name="b11_q7" value="D"> D. Không có</label>
      </div>
      <div class="quiz-explain">Giải thích: Tiên đề Euclid trong không gian: Trong không gian, qua một điểm không thuộc đường thẳng d cho trước, có một và chỉ một đường thẳng song song với d. Chọn A.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho tứ diện $ABCD$. Gọi $I, J$ lần lượt là trung điểm của $AC$ và $BC$; $K, L$ lần lượt là trung điểm của $AD$ và $BD$. Tứ giác $IJKL$ là hình gì?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b11_q8" value="A"> A. Hình vuông</label>
        <label class="quiz-option"><input type="radio" name="b11_q8" value="B"> B. Hình thang thường</label>
        <label class="quiz-option"><input type="radio" name="b11_q8" value="C"> C. Tứ giác không có cặp cạnh nào song song</label>
        <label class="quiz-option"><input type="radio" name="b11_q8" value="D"> D. Hình bình hành</label>
      </div>
      <div class="quiz-explain">Giải thích: $IJ$ là đường trung bình tam giác $ABC \Rightarrow IJ \parallel AB$ và $IJ = \frac{1}{2}AB$. $LK$ là đường trung bình tam giác $ABD \Rightarrow LK \parallel AB$ và $LK = \frac{1}{2}AB$. Tứ giác có một cặp cạnh đối vừa song song vừa bằng nhau là hình bình hành. Chọn D.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hai đường thẳng không có điểm chung thì có thể song song hoặc chéo nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Nếu đồng phẳng thì song song, nếu không đồng phẳng thì chéo nhau. Cả hai trường hợp đều không có điểm chung.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu hai đường thẳng không cắt nhau thì chúng nhất định phải song song với nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI NGU! Trong không gian, chúng hoàn toàn có thể CHÉO NHAU! Đây là bẫy kinh điển nhất của học sinh mất gốc.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu hai mặt phẳng cắt nhau và lần lượt chứa hai đường thẳng song song thì giao tuyến của chúng song song với hai đường thẳng đó (hoặc trùng với một trong hai). Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Đây chính là nội dung định lý giao tuyến của 3 mặt phẳng (SGK trang 81).</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Trong hình chóp $S.ABCD$, hai cạnh bên $SA$ và $SC$ là hai đường thẳng chéo nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Hai đường thẳng này CẮT NHAU tại đỉnh chung $S$, cùng nằm trong mặt phẳng $(SAC)$, không thể chéo nhau được.</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Trong hình chóp $S.ABCD$, cạnh bên $SA$ và cạnh đáy $BC$ là hai đường thẳng chéo nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Giả sử SA và BC đồng phẳng thì S phải thuộc mp(ABCD) $\Rightarrow$ vô lý. Do đó SA và BC không đồng phẳng $\Rightarrow$ chéo nhau.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Chứng minh song song</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang ($AB \parallel CD$, $AB = 2CD$). Gọi $M$ là trung điểm của $SA$. Gọi $N$ là trung điểm của $AB$. Chứng minh rằng $MN \parallel SC$ hoặc $MN \parallel CD$.</div>
      <textarea placeholder="Trình bày chứng minh dựa vào đường trung bình hoặc hình bình hành..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Trong tam giác $SAB$, $M$ là trung điểm $SA$ và $N$ là trung điểm $AB$.
        <br>&bull; Suy ra $MN$ là đường trung bình của tam giác $SAB \Rightarrow MN \parallel SB$.
        <br>&bull; Mặt khác, xét tứ giác $CDNB$: Vì $AB = 2CD$ và $N$ là trung điểm $AB$ nên $NB = \frac{1}{2}AB = CD$.
        <br>&bull; Lại có $NB \parallel CD$ (vì $N \in AB \parallel CD$).
        <br>&bull; Tứ giác $CDNB$ có một cặp cạnh đối vừa song song vừa bằng nhau ($NB = CD$ và $NB \parallel CD$) nên $CDNB$ là <strong>hình bình hành</strong>.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Quan sát chiếc cầu vượt đường bộ: làn đường trên cầu vượt và làn đường bên dưới mặt đất cắt ngang nhau. Hãy giải thích tại sao hai làn đường này không cắt nhau ngoài đời và mối quan hệ hình học của chúng là gì?</div>
      <textarea placeholder="Giải thích bằng khái niệm hai đường thẳng chéo nhau..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn kiến thức hình không gian:</strong>
        <br>&bull; Làn đường trên cầu vượt nằm trên một mặt phẳng lơ lửng ở cao độ $+6\text{ m}$.
        <br>&bull; Làn đường bên dưới mặt đất nằm trên mặt phẳng mặt đất ở cao độ $0\text{ m}$.
        <br>&bull; Hai đường thẳng này không cùng nằm trên bất kì mặt phẳng nào, do đó chúng là <strong>HAI ĐƯỜNG THẲNG CHÉO NHAU</strong>.
        <br>&bull; Nhờ tính chất chéo nhau trong không gian mà các phương tiện giao thông trên cầu và dưới gầm cầu có thể di chuyển đồng thời mà không bao giờ va chạm hay xung đột đường đi!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b11')">🏆 Chấm Điểm Bài 11 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""
