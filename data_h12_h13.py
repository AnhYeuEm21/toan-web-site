# -*- coding: utf-8 -*-
"""
data_h12_h13.py - BÀI 12 & BÀI 13 (CHƯƠNG IV HÌNH HỌC KHÔNG GIAN 11)
Bao gồm:
- Bài 12: Đường thẳng và mặt phẳng song song (SGK trang 84 - 88)
- Bài 13: Hai mặt phẳng song song (SGK trang 89 - 95)
Kèm 15 câu trắc nghiệm kiểm tra độ hiểu bài cho từng bài.
"""

H12_CONTENT = r"""
<section class="lesson-section" id="bai-12">
  <div class="lesson-header">
    <div class="lesson-number">12</div>
    <div class="lesson-meta">
      <h2>BÀI 12: ĐƯỜNG THẲNG VÀ MẶT PHẲNG SONG SONG</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương IV &bull; Trang 84 &ndash; 88</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Vị trí tương đối đường & mặt</span>
        <span class="lesson-tag">Phương pháp chứng minh d &parallel; (&alpha;)</span>
        <span class="lesson-tag">Định lý giao tuyến liên quan</span>
        <span class="lesson-tag">Thiết diện song song</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('hinh_08.png')">📖 Xem SGK Trang 84-85</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_09.png')">📖 Xem SGK Trang 86-88</button>
  </div>

  <!-- PHẦN 1: VỊ TRÍ TƯƠNG ĐỐI -->
  <h3 class="sec-title" id="h12-vi-tri-tuong-doi">1. Vị Trí Tương Đối Giữa Đường Thẳng Và Mặt Phẳng</h3>

  <div class="box box-theory">
    <div class="box-title">💡 BA TRẠNG THÁI QUAN HỆ GIỮA ĐƯỜNG VÀ MẶT</div>
    <ul class="content-list">
      <li><strong>1. Đường thẳng nằm trong mặt phẳng ($d \subset (\alpha)$):</strong>
        <br>&bull; Đường thẳng bám chặt trên mặt phẳng $\Rightarrow$ Có <strong>VÔ SỐ ĐIỂM CHUNG</strong>.
      </li>
      <li><strong>2. Đường thẳng cắt mặt phẳng ($d \cap (\alpha) = \{M\}$):</strong>
        <br>&bull; Đường thẳng đâm xuyên qua mặt phẳng $\Rightarrow$ Có <strong>ĐÚNG 1 ĐIỂM CHUNG DUY NHẤT</strong>.
      </li>
      <li><strong>3. Đường thẳng song song với mặt phẳng ($d \parallel (\alpha)$):</strong>
        <br>&bull; Đường thẳng bay lơ lửng bên trên hoặc bên dưới mặt phẳng $\Rightarrow$ <strong>HOÀN TOÀN KHÔNG CÓ ĐIỂM CHUNG NÀO</strong>!
      </li>
    </ul>
  </div>

  <!-- PHẦN 2: PHƯƠNG PHÁP VÀNG CHỨNG MINH ĐƯỜNG SONG SONG MẶT -->
  <h3 class="sec-title" id="h12-phuong-phap-chung-minh">2. Phương Pháp Vàng Chứng Minh Đường Song Song Mặt (SGK Trang 85)</h3>

  <div class="box box-formula">
    <div class="box-title">🔥 ĐỊNH LÝ 1: CÁCH DUY NHẤT ĐỂ CHỨNG MINH d &parallel; (&alpha;) TRONG BÀI THI</div>
    <div class="formula-display">
      <span style="display:inline-block;vertical-align:middle;text-align:left;">
        &bull; Đường thẳng d KHÔNG NẰM TRONG (&alpha;)<br>
        &bull; Tìm được một đường thẳng d' NẰM TRONG (&alpha;)<br>
        &bull; Sao cho d &parallel; d'
      </span>
      &nbsp;&nbsp;&rArr;&nbsp;&nbsp;
      <strong style="color:var(--accent-green);font-size:1.15rem;">d &parallel; (&alpha;)</strong>
    </div>
    <div class="formula-label">Thần chú nhớ: "Muốn song song với mặt &ndash; Chỉ cần song song với một đường nằm trong mặt là xong!"</div>
  </div>

  <div class="box box-warning">
    <div class="box-title">⚠️ BẪY MẤT ĐIỂM OAN UỔNG CỦA HỌC SINH</div>
    <p>Rất nhiều đứa chứng minh $d \parallel d'$ xong kết luận luôn $d \parallel (\alpha)$. Thầy cô sẽ gạch ngay và trừ 0,5 điểm!</p>
    <p style="margin-top:6px;"><strong>LÝ DO:</strong> Mày quên mất điều kiện sống còn: <strong>$d$ KHÔNG ĐƯỢC NẰM TRONG $(\alpha)$</strong> ($d \not\subset (\alpha)$). Nếu lỡ $d$ nằm trọn trong $(\alpha)$ thì làm sao song song được nữa! Phải ghi đủ 3 dòng thì mới được trọn vẹn điểm tối đa.</p>
  </div>

  <!-- PHẦN 3: ĐỊNH LÝ GIAO TUYẾN LIÊN QUAN -->
  <h3 class="sec-title" id="h12-dinh-ly-giao-tuyen">3. Định Lý Giao Tuyến Của Mặt Phẳng Chứa Đường Song Song</h3>

  <div class="box box-formula">
    <div class="box-title">📐 ĐỊNH LÝ 2: TẠO RA GIAO TUYẾN SONG SONG (SGK Trang 86)</div>
    <div class="formula-display">
      Nếu d &parallel; (&alpha;)  và  mặt phẳng (&beta;) chứa d cắt (&alpha;) theo giao tuyến d'   &rArr;   <strong style="color:var(--accent-yellow);">d' &parallel; d</strong>
    </div>
    <div class="formula-label">Ứng dụng: Chuyên dùng để vẽ giao tuyến và tìm thiết diện khi cắt hình chóp bằng một mặt phẳng!</div>
  </div>

  <!-- PHẦN 4: THỰC CHIẾN BÀI 12 -->
  <h3 class="sec-title" id="h12-thuc-chien">4. Thực Chiến Giải Bài Tập Mẫu Bài 12 (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP: CHỨNG MINH ĐƯỜNG THẲNG SONG SONG VỚI MẶT PHẲNG QUA TRUNG ĐIỂM</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M$ là trung điểm của cạnh bên $SA$. Chứng minh rằng đường thẳng $OM \parallel (SCD)$ (với $O$ là giao điểm của $AC$ và $BD$).</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi đường thẳng nằm trong $(SCD)$ mà $OM$ có cơ hội song song</strong>
          <p>Mặt phẳng $(SCD)$ có 3 cạnh là $SC, CD, SD$. Nhìn vào $OM$: điểm $M$ nằm trên $SA$, điểm $O$ nằm trên $AC$. Vậy $OM$ nằm trong tam giác $SAC$!</p>
          <p>Trong tam giác $SAC$, cạnh đối diện với $SA$ chính là cạnh <strong>$SC$</strong> (thuộc mặt phẳng $(SCD)$)!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Dùng bảo bối lớp 10 (Đường trung bình) chứng minh $OM \parallel SC$</strong>
          <p>&bull; $M$ là trung điểm của $SA$ (đề bài cho).</p>
          <p>&bull; $ABCD$ là hình bình hành nên hai đường chéo $AC$ và $BD$ cắt nhau tại trung điểm của mỗi đường $\Rightarrow O$ là trung điểm của $AC$!</p>
          <p>&bull; Trong tam giác $SAC$, có $M$ là trung điểm $SA$ và $O$ là trung điểm $AC \Rightarrow OM$ là <strong>đường trung bình của tam giác $SAC$</strong>!</p>
          <p>&bull; Suy ra: <strong>$OM \parallel SC$</strong>.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Trình bày kết luận 3 dòng chuẩn chỉnh</strong>
          <p>Ta có:</p>
          <p>&bull; $OM \parallel SC$ (chứng minh trên).</p>
          <p>&bull; $SC \subset (SCD)$.</p>
          <p>&bull; $OM \not\subset (SCD)$ (vì $O$ và $M$ không nằm trên $(SCD)$).</p>
          <p>$\Rightarrow \mathbf{OM \parallel (SCD)}$ (điều phải chứng minh!). Đẹp không tì vết!</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 5: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 12 -->
  <div class="quiz-section" id="b12-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 12 (15 CÂU)</div>
        <div class="quiz-sub">Phương pháp chứng minh d // (P), số điểm chung, định lý giao tuyến &bull; Đạt 12/15 là giỏi!</div>
      </div>
      <div class="quiz-score-badge" id="b12-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nếu đường thẳng $d$ song song với mặt phẳng $(\alpha)$ thì số điểm chung giữa $d$ và $(\alpha)$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q1" value="A"> A. $0$ điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b12_q1" value="B"> B. $1$ điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b12_q1" value="C"> C. $2$ điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b12_q1" value="D"> D. Vô số điểm chung</label>
      </div>
      <div class="quiz-explain">Giải thích: Đường thẳng song song với mặt phẳng nghĩa là chúng không có bất kì điểm chung nào ($d \cap (\alpha) = \emptyset$). Chọn A.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Điều kiện nào sau đây là ĐỦ để kết luận đường thẳng $d$ song song với mặt phẳng $(\alpha)$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q2" value="A"> A. $d$ song song với một đường thẳng $d'$ bất kì</label>
        <label class="quiz-option"><input type="radio" name="b12_q2" value="B"> B. $d$ không có điểm chung với đường thẳng $d'$ nằm trong $(\alpha)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q2" value="C"> C. $d \not\subset (\alpha)$ và $d$ song song với một đường thẳng $d' \subset (\alpha)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q2" value="D"> D. $d$ vuông góc với mặt phẳng $(\alpha)$</label>
      </div>
      <div class="quiz-explain">Giải thích: Định lý nhận biết: Phải thỏa mãn đồng thời $d \not\subset (\alpha)$ và $d \parallel d' \subset (\alpha)$. Chọn C.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Đường thẳng $AB$ song song với mặt phẳng nào sau đây?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q3" value="A"> A. $(SAB)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q3" value="B"> B. $(SCD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q3" value="C"> C. $(SAD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q3" value="D"> D. $(SBC)$</label>
      </div>
      <div class="quiz-explain">Giải thích: Vì $AB \parallel CD$ mà $CD \subset (SCD)$ và $AB \not\subset (SCD)$ nên $AB \parallel (SCD)$. Chọn B.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho tứ diện $ABCD$. Gọi $M, N$ lần lượt là trung điểm của $AB$ và $AC$. Đường thẳng $MN$ song song với mặt phẳng nào?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q4" value="A"> A. $(ABC)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q4" value="B"> B. $(ABD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q4" value="C"> C. $(ACD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q4" value="D"> D. $(BCD)$</label>
      </div>
      <div class="quiz-explain">Giải thích: $MN$ là đường trung bình của tam giác $ABC \Rightarrow MN \parallel BC$. Mà $BC \subset (BCD)$ và $MN \not\subset (BCD) \Rightarrow MN \parallel (BCD)$. Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nếu đường thẳng $d \parallel (\alpha)$ thì trong mặt phẳng $(\alpha)$ có bao nhiêu đường thẳng song song với $d$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q5" value="A"> A. Vô số đường thẳng</label>
        <label class="quiz-option"><input type="radio" name="b12_q5" value="B"> B. Duy nhất 1 đường thẳng</label>
        <label class="quiz-option"><input type="radio" name="b12_q5" value="C"> C. 2 đường thẳng</label>
        <label class="quiz-option"><input type="radio" name="b12_q5" value="D"> D. Không có đường thẳng nào</label>
      </div>
      <div class="quiz-explain">Giải thích: Bất kì đường thẳng nào song song với hình chiếu của d trên (alpha) hoặc qua mỗi điểm trong (alpha) kẻ đường thẳng song song với d đều nằm trong (alpha). Do đó có vô số đường! Chọn A.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho đường thẳng $d \parallel (\alpha)$. Mặt phẳng $(\beta)$ chứa $d$ cắt $(\alpha)$ theo giao tuyến $c$. Khẳng định nào ĐÚNG?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q6" value="A"> A. $c$ cắt $d$</label>
        <label class="quiz-option"><input type="radio" name="b12_q6" value="B"> B. $c \parallel d$</label>
        <label class="quiz-option"><input type="radio" name="b12_q6" value="C"> C. $c$ chéo nhau với $d$</label>
        <label class="quiz-option"><input type="radio" name="b12_q6" value="D"> D. $c \equiv d$</label>
      </div>
      <div class="quiz-explain">Giải thích: Định lý 2 SGK trang 86: Giao tuyến c phải song song với d. Chọn B.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hai mặt phẳng phân biệt cùng song song với một đường thẳng thì giao tuyến của chúng (nếu có) sẽ:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q7" value="A"> A. Cắt đường thẳng đó</label>
        <label class="quiz-option"><input type="radio" name="b12_q7" value="B"> B. Chéo nhau với đường thẳng đó</label>
        <label class="quiz-option"><input type="radio" name="b12_q7" value="C"> C. Song song với đường thẳng đó</label>
        <label class="quiz-option"><input type="radio" name="b12_q7" value="D"> D. Vuông góc với đường thẳng đó</label>
      </div>
      <div class="quiz-explain">Giải thích: Hệ quả định lý: Nếu $(\alpha) \parallel d$ và $(\beta) \parallel d$ thì giao tuyến $d' = (\alpha) \cap (\beta)$ thỏa mãn $d' \parallel d$. Chọn C.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $G$ là trọng tâm tam giác $SAB$. Đường thẳng qua $G$ song song với $AB$ sẽ song song với mặt phẳng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b12_q8" value="A"> A. $(ABCD)$ và $(SCD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q8" value="B"> B. $(SAD)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q8" value="C"> C. $(SBC)$</label>
        <label class="quiz-option"><input type="radio" name="b12_q8" value="D"> D. $(SAC)$</label>
      </div>
      <div class="quiz-explain">Giải thích: Đường thẳng d qua G song song với AB. Vì $AB \parallel CD$ nên $d$ song song với cả AB (thuộc ABCD) và CD (thuộc SCD), mà d không nằm trong 2 mặt này nên $d \parallel (ABCD)$ và $d \parallel (SCD)$. Chọn A.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu đường thẳng $d$ song song với một đường thẳng $a$ nằm trong $(\alpha)$ thì $d$ nhất định phải song song với $(\alpha)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI THIẾU ĐIỀU KIỆN! Nhỡ đường thẳng d nằm luôn trong (alpha) thì sao! Phải có thêm điều kiện $d \not\subset (\alpha)$ mới đúng.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu đường thẳng $d$ song song với mặt phẳng $(\alpha)$ thì $d$ không có điểm chung nào với $(\alpha)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Đây chính là định nghĩa đường thẳng song song với mặt phẳng.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Trong hình chóp $S.ABCD$ có đáy là hình bình hành, đường thẳng nối trung điểm của $SA$ và $SD$ song song với mặt phẳng đáy $(ABCD)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Gọi trung điểm là M, N thì $MN \parallel AD$ (đường trung bình $\Delta SAD$). Vì $AD \subset (ABCD)$ và $MN \not\subset (ABCD)$ nên $MN \parallel (ABCD)$.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu $d \parallel (\alpha)$ thì $d$ song song với mọi đường thẳng nằm trong $(\alpha)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI NGU! Trong (alpha) có vô số đường thẳng CHÉO NHAU với d! Nó chỉ song song với các đường thẳng có cùng phương với nó mà thôi.</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Qua một điểm nằm ngoài mặt phẳng $(\alpha)$, có vô số đường thẳng song song với $(\alpha)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tất cả các đường thẳng đi qua điểm đó và nằm trong mặt phẳng song song với (alpha) đều song song với (alpha). Có vô số đường như vậy!</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Chứng minh song song</div>
      <div class="quiz-q-text">Cho tứ diện $ABCD$. Gọi $G$ là trọng tâm tam giác $ABD$. Trên đoạn $BC$ lấy điểm $E$ sao cho $BE = \frac{1}{3}BC$. Gọi $I$ là trung điểm của $BD$. Chứng minh $GE \parallel (ACD)$ hoặc $GI \parallel (BCD)$.</div>
      <textarea placeholder="Trình bày bài giải dựa vào tỉ lệ trọng tâm..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Trong tam giác $ABD$, $I$ là trung điểm của $BD$ nên $AI$ là đường trung tuyến.
        <br>&bull; Vì $G$ là trọng tâm tam giác $ABD$ nên ta có tỉ lệ: $\frac{IG}{IA} = \frac{1}{3}$.
        <br>&bull; Mặt khác, trên cạnh $BC$ có $BE = \frac{1}{3}BC \Rightarrow \frac{BE}{BC} = \frac{1}{3}$.
        <br>&bull; Trong tam giác $ABC$ hoặc xét mặt phẳng phụ, áp dụng định lý Thales đảo sẽ suy ra đường thẳng song song với một đường thẳng của mặt phẳng tương ứng, từ đó suy ra quan hệ song song với mặt phẳng.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Một bóng đèn tuýp dài được treo nằm ngang song song với sàn nhà. Bóng của bóng đèn tuýp in trên mặt sàn có song song với bóng đèn hay không? Giải thích bằng định lý hình học không gian.</div>
      <textarea placeholder="Giải thích bằng giao tuyến của mặt phẳng ánh sáng với sàn nhà..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn hình học không gian:</strong>
        <br>&bull; Gọi đường thẳng bóng đèn tuýp là $d$. Sàn nhà là mặt phẳng $(P)$. Đề cho $d \parallel (P)$.
        <br>&bull; Chùm ánh sáng hoặc mặt phẳng chiếu thẳng đứng đi qua bóng đèn $d$ cắt mặt sàn $(P)$ tạo ra bóng in của bóng đèn chính là giao tuyến $d'$.
        <br>&bull; Theo định lý 2 về giao tuyến: Mặt phẳng chứa $d$ cắt $(P)$ theo giao tuyến $d'$ thì BẮT BUỘC $d' \parallel d$.
        <br>&bull; Do đó bóng in trên sàn nhà luôn song song với bóng đèn tuýp!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b12')">🏆 Chấm Điểm Bài 12 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""

H13_CONTENT = r"""
<section class="lesson-section" id="bai-13">
  <div class="lesson-header">
    <div class="lesson-number">13</div>
    <div class="lesson-meta">
      <h2>BÀI 13: HAI MẶT PHẲNG SONG SONG</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương IV &bull; Trang 89 &ndash; 95</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Hai mặt phẳng song song</span>
        <span class="lesson-tag">Phương pháp chứng minh (P) &parallel; (Q)</span>
        <span class="lesson-tag">Định lý Thales không gian</span>
        <span class="lesson-tag">Hình lăng trụ & Hình hộp</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('hinh_10.png')">📖 Xem SGK Trang 89-90</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_11.png')">📖 Xem SGK Trang 91-92</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_12.png')">📖 Xem SGK Trang 93-94</button>
    <button class="sgk-btn" onclick="openSgkModal('hinh_13.png')">📖 Xem SGK Trang 95</button>
  </div>

  <!-- PHẦN 1: ĐỊNH NGHĨA HAI MẶT PHẲNG SONG SONG -->
  <h3 class="sec-title" id="h13-dinh-nghia">1. Định Nghĩa Hai Mặt Phẳng Song Song (Hai Tấm Gương Song Hành)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: SÀN NHÀ VÀ TRẦN NHÀ</div>
    <p>Hai mặt phẳng được gọi là song song với nhau nếu chúng <strong>KHÔNG CÓ ĐIỂM CHUNG NÀO</strong>! Kí hiệu: $(P) \parallel (Q)$.</p>
    <p style="margin-top:6px;">Hình ảnh ngoài đời: Sàn nhà và trần nhà của căn phòng, hai bề mặt của bức tường đôi, hay hai mặt của tấm ván ép phẳng lỳ.</p>
  </div>

  <!-- PHẦN 2: PHƯƠNG PHÁP VÀNG CHỨNG MINH 2 MẶT SONG SONG -->
  <h3 class="sec-title" id="h13-phuong-phap-chung-minh">2. Phương Pháp Vàng Chứng Minh Hai Mặt Song Song (SGK Trang 90)</h3>

  <div class="box box-formula">
    <div class="box-title">🔥 ĐỊNH LÝ 1: CÁCH DUY NHẤT ĐỂ CHỨNG MINH (P) &parallel; (Q) TRONG ĐỀ THI</div>
    <div class="formula-display">
      <span style="display:inline-block;vertical-align:middle;text-align:left;">
        &bull; Mặt phẳng (P) chứa hai đường thẳng a và b<br>
        &bull; a và b CẮT NHAU tại một điểm<br>
        &bull; a &parallel; (Q)<br>
        &bull; b &parallel; (Q)
      </span>
      &nbsp;&nbsp;&rArr;&nbsp;&nbsp;
      <strong style="color:var(--accent-green);font-size:1.15rem;">(P) &parallel; (Q)</strong>
    </div>
    <div class="formula-label">Thần chú sống còn: "TÌM 2 ĐƯỜNG CẮT NHAU NẰM TRONG MẶT NÀY &ndash; CÙNG SONG SONG VỚI MẶT KIA!"</div>
  </div>

  <div class="box box-warning">
    <div class="box-title">⚠️ BẪY TỬ THẦN: QUÊN TỪ "CẮT NHAU"</div>
    <p>Nhiều học sinh vội vàng tìm được $a \parallel (Q)$ và $b \parallel (Q)$, nhưng $a$ và $b$ lại là <strong>HAI ĐƯỜNG THẲNG SONG SONG VỚI NHAU</strong>! Lúc đó mặt phẳng $(P)$ có thể vẫn CẮT $(Q)$!</p>
    <p style="margin-top:6px;">BẮT BUỘC hai đường thẳng $a$ và $b$ phải <strong>CẮT NHAU</strong> (tạo thành một chiếc kiềng 2 chân vững chãi trong mặt phẳng) thì mới khóa chặt được quan hệ song song!</p>
  </div>

  <!-- PHẦN 3: CÁC TÍNH CHẤT KINH ĐIỂN CỦA HAI MẶT SONG SONG -->
  <h3 class="sec-title" id="h13-tinh-chat">3. Các Tính Chất Kinh Điển (Dùng Làm Bài Toán Tính Toán)</h3>

  <div class="box box-formula">
    <div class="box-title">📐 BỘ BA TÍNH CHẤT BẤT BIẾN (SGK Trang 91)</div>
    <ul class="content-list">
      <li><strong>Tính chất 1 (Duy nhất):</strong> Qua một điểm nằm ngoài một mặt phẳng, có một và chỉ một mặt phẳng song song với mặt phẳng đã cho.</li>
      <li><strong>Tính chất 2 (Cắt tạo giao tuyến song song):</strong> Nếu hai mặt phẳng song song bị cắt bởi một mặt phẳng thứ ba thì <strong>hai giao tuyến tạo thành song song với nhau</strong>!
        <br><div class="formula-display" style="font-size:0.95rem;">(P) &parallel; (Q)  và  (R) c&abreve;t (P), (Q) theo giao tuyến a, b   &rArr;   a &parallel; b</div>
      </li>
      <li><strong>Tính chất 3 (Đoạn chắn bằng nhau):</strong> Hai đoạn thẳng song song bị chắn giữa hai mặt phẳng song song thì <strong>bằng nhau</strong> ($AB = CD$).</li>
    </ul>
  </div>

  <!-- PHẦN 4: HÌNH LĂNG TRỤ VÀ HÌNH HỘP -->
  <h3 class="sec-title" id="h13-lang-tru-hop">4. Hình Lăng Trụ & Hình Hộp (Toàn Bộ Định Nghĩa & Tính Chất)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: LĂNG TRỤ VÀ HÌNH HỘP LÀ GÌ?</div>
    <ul class="content-list">
      <li><strong>HÌNH LĂNG TRỤ $A_1 A_2 ... A_n . A'_1 A'_2 ... A'_n$:</strong>
        <br>&bull; Có <strong>hai mặt đáy song song và bằng nhau</strong> (ví dụ lăng trụ tam giác thì hai đáy là hai tam giác bằng nhau).
        <br>&bull; Các mặt bên <strong>LUÔN LUÔN LÀ CÁC HÌNH BÌNH HÀNH</strong>.
        <br>&bull; Các cạnh bên <strong>SONG SONG VÀ BẰNG NHAU</strong> ($AA' = BB' = CC'$ và $AA' \parallel BB' \parallel CC'$).
      </li>
      <li><strong>HÌNH HỘP $ABCD.A'B'C'D'$:</strong>
        <br>&bull; Là hình lăng trụ có <strong>mặt đáy là hình bình hành</strong>!
        <br>&bull; Đặc điểm thần thánh: <strong>CẢ 6 MẶT ĐỀU LÀ HÌNH BÌNH HÀNH!</strong>
        <br>&bull; Hai mặt đối diện song song và bằng nhau.
        <br>&bull; Bốn đường chéo ($AC', BD', CA', DB'$) <strong>CẮT NHAU TẠI TRUNG ĐIỂM MỖI ĐƯỜNG</strong> (điểm này gọi là tâm của hình hộp!).
      </li>
    </ul>
  </div>

  <!-- PHẦN 5: THỰC CHIẾN BÀI 13 -->
  <h3 class="sec-title" id="h13-thuc-chien">5. Thực Chiến Giải Bài Tập Mẫu Bài 13 (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP: CHỨNG MINH HAI MẶT PHẲNG SONG SONG</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $M, N, P$ lần lượt là trung điểm của các cạnh bên $SA, SB, SC$. Chứng minh rằng mặt phẳng $(MNP) \parallel (ABCD)$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Tìm 2 đường thẳng cắt nhau trong $(MNP)$</strong>
          <p>Mặt phẳng $(MNP)$ chứa các đường thẳng $MN, NP, MP$. Rõ ràng $MN$ và $NP$ cắt nhau tại điểm $N$!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Chứng minh từng đường song song với mặt phẳng đáy $(ABCD)$</strong>
          <p>&bull; Trong tam giác $SAB$: $M, N$ là trung điểm $SA, SB \Rightarrow MN$ là đường trung bình $\Rightarrow MN \parallel AB$.</p>
          <p>Mà $AB \subset (ABCD)$ và $MN \not\subset (ABCD) \Rightarrow \mathbf{MN \parallel (ABCD)}$.</p>
          <p>&bull; Trong tam giác $SBC$: $N, P$ là trung điểm $SB, SC \Rightarrow NP$ là đường trung bình $\Rightarrow NP \parallel BC$.</p>
          <p>Mà $BC \subset (ABCD)$ và $NP \not\subset (ABCD) \Rightarrow \mathbf{NP \parallel (ABCD)}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Tổng hợp điều kiện để kết luận $(MNP) \parallel (ABCD)$</strong>
          <p>Trong mặt phẳng $(MNP)$, có hai đường thẳng $MN$ và $NP$ cắt nhau tại $N$.</p>
          <p>Cả $MN$ và $NP$ đều song song với mặt phẳng $(ABCD)$.</p>
          <p>Theo định lý nhận biết: <strong>$(MNP) \parallel (ABCD)$</strong>. Xong bài chuẩn chỉnh!</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHẦN 6: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 13 -->
  <div class="quiz-section" id="b13-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 13 (15 CÂU)</div>
        <div class="quiz-sub">Hai mặt phẳng song song, hình lăng trụ, hình hộp &bull; Đạt 12/15 là thành cao thủ!</div>
      </div>
      <div class="quiz-score-badge" id="b13-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Hai mặt phẳng được gọi là song song với nhau nếu:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q1" value="A"> A. Chúng có duy nhất một điểm chung</label>
        <label class="quiz-option"><input type="radio" name="b13_q1" value="B"> B. Chúng không có điểm chung nào</label>
        <label class="quiz-option"><input type="radio" name="b13_q1" value="C"> C. Chúng có 2 điểm chung phân biệt</label>
        <label class="quiz-option"><input type="radio" name="b13_q1" value="D"> D. Chúng cắt nhau theo một đường thẳng</label>
      </div>
      <div class="quiz-explain">Giải thích: Định nghĩa SGK trang 89: Hai mặt phẳng song song là hai mặt phẳng không có điểm chung nào. Chọn B.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Khẳng định nào sau đây là ĐÚNG về điều kiện để $(P) \parallel (Q)$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q2" value="A"> A. $(P)$ chứa hai đường thẳng cắt nhau cùng song song với $(Q)$</label>
        <label class="quiz-option"><input type="radio" name="b13_q2" value="B"> B. $(P)$ chứa hai đường thẳng song song cùng song song với $(Q)$</label>
        <label class="quiz-option"><input type="radio" name="b13_q2" value="C"> C. $(P)$ chứa một đường thẳng song song với $(Q)$</label>
        <label class="quiz-option"><input type="radio" name="b13_q2" value="D"> D. $(P)$ có một điểm chung với $(Q)$</label>
      </div>
      <div class="quiz-explain">Giải thích: Bắt buộc hai đường thẳng đó phải CẮT NHAU trong (P) và cùng song song với (Q). Chọn A.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Các mặt bên của một hình lăng trụ LUÔN LUÔN là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q3" value="A"> A. Hình tam giác</label>
        <label class="quiz-option"><input type="radio" name="b13_q3" value="B"> B. Hình chữ nhật</label>
        <label class="quiz-option"><input type="radio" name="b13_q3" value="C"> C. Hình bình hành</label>
        <label class="quiz-option"><input type="radio" name="b13_q3" value="D"> D. Hình vuông</label>
      </div>
      <div class="quiz-explain">Giải thích: Theo định nghĩa hình lăng trụ SGK trang 93: Các mặt bên của hình lăng trụ luôn luôn là các hình bình hành. Chọn C.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Một hình hộp có tổng cộng bao nhiêu mặt và bao nhiêu đỉnh?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q4" value="A"> A. 4 mặt, 6 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b13_q4" value="B"> B. 5 mặt, 6 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b13_q4" value="C"> C. 6 mặt, 6 đỉnh</label>
        <label class="quiz-option"><input type="radio" name="b13_q4" value="D"> D. 6 mặt, 8 đỉnh</label>
      </div>
      <div class="quiz-explain">Giải thích: Hình hộp ABCD.A'B'C'D' có 6 mặt (đều là hình bình hành), 8 đỉnh và 12 cạnh. Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Bốn đường chéo của hình hộp có tính chất nào sau đây?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q5" value="A"> A. Đôi một vuông góc với nhau</label>
        <label class="quiz-option"><input type="radio" name="b13_q5" value="B"> B. Cắt nhau tại trung điểm của mỗi đường</label>
        <label class="quiz-option"><input type="radio" name="b13_q5" value="C"> C. Luôn có độ dài bằng nhau</label>
        <label class="quiz-option"><input type="radio" name="b13_q5" value="D"> D. Đôi một chéo nhau</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất hình hộp SGK trang 94: Bốn đường chéo của hình hộp cắt nhau tại trung điểm của mỗi đường (điểm này gọi là tâm hình hộp). Chọn B.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Nếu hai mặt phẳng $(P)$ và $(Q)$ song song với nhau thì một mặt phẳng $(R)$ cắt $(P)$ theo giao tuyến $a$ và cắt $(Q)$ theo giao tuyến $b$. Mối quan hệ giữa $a$ và $b$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q6" value="A"> A. $a \parallel b$</label>
        <label class="quiz-option"><input type="radio" name="b13_q6" value="B"> B. $a$ cắt $b$</label>
        <label class="quiz-option"><input type="radio" name="b13_q6" value="C"> C. $a$ chéo nhau với $b$</label>
        <label class="quiz-option"><input type="radio" name="b13_q6" value="D"> D. $a \equiv b$</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất SGK: Hai mặt phẳng song song bị cắt bởi mặt phẳng thứ ba thì tạo ra hai giao tuyến song song ($a \parallel b$). Chọn A.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Qua một điểm nằm ngoài mặt phẳng $(P)$, có bao nhiêu mặt phẳng song song với $(P)$?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q7" value="A"> A. Không có</label>
        <label class="quiz-option"><input type="radio" name="b13_q7" value="B"> B. Vô số</label>
        <label class="quiz-option"><input type="radio" name="b13_q7" value="C"> C. Duy nhất 1 mặt phẳng</label>
        <label class="quiz-option"><input type="radio" name="b13_q7" value="D"> D. 2 mặt phẳng</label>
      </div>
      <div class="quiz-explain">Giải thích: Tính chất 1 SGK trang 91: Qua một điểm nằm ngoài một mặt phẳng cho trước, có một và chỉ một mặt phẳng song song với mặt phẳng đó. Chọn C.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho hình lăng trụ tam giác $ABC.A'B'C'$. Cặp mặt phẳng nào sau đây SONG SONG với nhau?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b13_q8" value="A"> A. $(ABB'A')$ và $(ACC'A')$</label>
        <label class="quiz-option"><input type="radio" name="b13_q8" value="B"> B. $(ABC)$ và $(ABB'A')$</label>
        <label class="quiz-option"><input type="radio" name="b13_q8" value="C"> C. $(BCC'B')$ và $(A'B'C')$</label>
        <label class="quiz-option"><input type="radio" name="b13_q8" value="D"> D. $(ABC)$ và $(A'B'C')$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hai mặt đáy của hình lăng trụ luôn luôn song song với nhau: $(ABC) \parallel (A'B'C')$. Chọn D.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Tất cả các cạnh bên của một hình lăng trụ luôn song song và bằng nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Định nghĩa lăng trụ: Các cạnh bên là các đoạn thẳng song song và bằng nhau.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu mặt phẳng $(P)$ chứa hai đường thẳng song song với $(Q)$ thì $(P) \parallel (Q)$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Hai đường thẳng đó phải CẮT NHAU! Nếu 2 đường đó song song với nhau thì (P) vẫn có thể cắt (Q).</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hai mặt phẳng phân biệt cùng song song với mặt phẳng thứ ba thì song song với nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Tính chất bắc cầu: Nếu $(P) \parallel (R)$ và $(Q) \parallel (R)$ với $(P) \ne (Q)$ thì $(P) \parallel (Q)$.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hình hộp là hình lăng trụ có đáy là hình tam giác. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Hình hộp là hình lăng trụ có đáy là HÌNH BÌNH HÀNH (tứ giác), không phải tam giác!</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Hai đoạn thẳng song song bị chắn giữa hai mặt phẳng song song thì có độ dài bằng nhau. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Chúng tạo thành các cạnh đối của một hình bình hành nên bằng nhau.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Hình lăng trụ</div>
      <div class="quiz-q-text">Cho hình lăng trụ tam giác $ABC.A'B'C'$. Gọi $M, M'$ lần lượt là trung điểm của các cạnh $BC$ và $B'C'$. Chứng minh rằng tứ giác $BMM'B'$ là hình bình hành và mặt phẳng $(AMM'A')$ cắt hình lăng trụ thành hai hình gì?</div>
      <textarea placeholder="Chứng minh BMM'B' là hình bình hành..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Ta có $BB' \parallel CC'$ và $BB' = CC'$ (tính chất lăng trụ).
        <br>&bull; Vì $M$ là trung điểm $BC$ và $M'$ là trung điểm $B'C'$ nên $BM = \frac{1}{2}BC = \frac{1}{2}B'C' = B'M'$.
        <br>&bull; Đồng thời $BM \parallel B'M'$ (vì nằm trên $BC$ và $B'C'$ song song).
        <br>&bull; Tứ giác $BMM'B'$ có một cặp cạnh đối vừa song song vừa bằng nhau ($BM = B'M'$ và $BM \parallel B'M'$) nên $BMM'B'$ là <strong>hình bình hành</strong>.
        <br>&bull; Mặt phẳng $(AMM'A')$ chia lăng trụ tam giác $ABC.A'B'C'$ thành hai hình lăng trụ tam giác nhỏ hơn: $ABM.A'B'M'$ và $ACM.A'C'M'$.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng thực tế</div>
      <div class="quiz-q-text">Một chiếc thang xương cá có các bậc thang nằm trên tường song song với nhau. Giải thích tại sao các mép bậc thang lại song song với nhau dựa trên tính chất giao tuyến của các mặt phẳng song song.</div>
      <textarea placeholder="Giải thích dựa trên giao tuyến với tường nhà..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn kiến thức hình học không gian:</strong>
        <br>&bull; Bề mặt của các bậc thang là các mặt phẳng song song với nhau (để khi bước chân lên không bị nghiêng ngả): $(P_1) \parallel (P_2) \parallel (P_3)...$
        <br>&bull; Bức tường nhà dựng đứng đóng vai trò là một mặt phẳng thứ ba $(\alpha)$ cắt các mặt phẳng bậc thang này.
        <br>&bull; Theo định lý: Khi một mặt phẳng cắt các mặt phẳng song song thì các giao tuyến tạo thành PHẢI SONG SONG VỚI NHAU.
        <br>&bull; Các mép bậc thang gắn vào tường chính là các giao tuyến đó, vì vậy chúng luôn song song với nhau một cách tuyệt đối!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b13')">🏆 Chấm Điểm Bài 13 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""
