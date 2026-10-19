# -*- coding: utf-8 -*-
"""
data_b1_b2.py - BÀI 1 & BÀI 2 (CHƯƠNG I ĐẠI SỐ 11)
Bao gồm:
- Bài 1: Giá trị lượng giác của góc lượng giác (SGK trang 5 - 15)
- Bài 2: Công thức lượng giác (SGK trang 16 - 21)
Kèm 15 câu trắc nghiệm kiểm tra độ hiểu bài cho từng bài.
"""

B1_CONTENT = r"""
<section class="lesson-section" id="bai-1">
  <div class="lesson-header">
    <div class="lesson-number">1</div>
    <div class="lesson-meta">
      <h2>BÀI 1: GIÁ TRỊ LƯỢNG GIÁC CỦA GÓC LƯỢNG GIÁC</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương I &bull; Trang 5 &ndash; 15</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Góc lượng giác</span>
        <span class="lesson-tag">Đơn vị Radian</span>
        <span class="lesson-tag">Hệ thức Chasles</span>
        <span class="lesson-tag">Đường tròn lượng giác</span>
        <span class="lesson-tag">Cos đối - Sin bù - Phụ chéo</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('page_01.png')">📖 Xem SGK Trang 5</button>
    <button class="sgk-btn" onclick="openSgkModal('page_02.png')">📖 Xem SGK Trang 6-7</button>
    <button class="sgk-btn" onclick="openSgkModal('page_03.png')">📖 Xem SGK Trang 8-9</button>
    <button class="sgk-btn" onclick="openSgkModal('page_04.png')">📖 Xem SGK Trang 10-11</button>
    <button class="sgk-btn" onclick="openSgkModal('page_05.png')">📖 Xem SGK Trang 12-13</button>
    <button class="sgk-btn" onclick="openSgkModal('page_06.png')">📖 Xem SGK Trang 14-15</button>
  </div>

  <!-- PHẦN 1: KHÁI NIỆM GÓC LƯỢNG GIÁC -->
  <h3 class="sec-title" id="b1-goc-luong-giac">1. "Dịch" Góc Lượng Giác Sang Tiếng Người (Băm Nát Định Nghĩa)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 TẠI SAO LẠI SINH RA "GÓC LƯỢNG GIÁC"?</div>
    <p>Hồi cấp 2, mày học <strong>góc hình học</strong> (như cái quạt nan mở ra): hai tia $Ou$ và $Ov$ đứng im một chỗ, góc cùng lắm từ $0^\circ$ đến $180^\circ$ (góc bẹt), đố kiếm đâu ra góc âm hay góc $720^\circ$!</p>
    <p style="margin-top:8px;">Nhưng ở ngoài đời, cái kim đồng hồ quay liên tục, bánh xe đạp lăn hàng nghìn vòng, cánh quạt gió xoay tít mù. Làm sao dùng cái góc cụt ngủn $180^\circ$ để mô tả được? Thế là người ta phát minh ra <strong>GÓC LƯỢNG GIÁC</strong>:</p>
    <ul class="content-list">
      <li>Cho tia đầu $Ou$ đứng im làm mốc xuất phát.</li>
      <li>Tia $Om$ ban đầu đè lên $Ou$, sau đó bắt đầu <strong>QUAY</strong> quanh điểm $O$ cho tới khi dừng lại trùng khít với tia cuối $Ov$.</li>
      <li>Góc mà tia $Om$ quét được trong quá trình quay đó chính là một <span class="tooltip" data-tip="Góc được tạo ra bởi sự chuyển động quay của một tia từ vị trí đầu đến vị trí cuối">góc lượng giác</span>, kí hiệu là $(Ou, Ov)$.</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 QUY TẮC DẤU CHIỀU QUAY (QUY ƯỚC QUỐC TẾ BẮT BUỘC)</div>
    <div class="formula-display">
      <span style="color:var(--accent-green);">QUAY NGƯỢC CHIỀU KIM ĐỒNG HỒ = DƯƠNG (+)</span><br>
      <span style="color:var(--accent-red);margin-top:6px;display:inline-block;">QUAY CÙNG CHIỀU KIM ĐỒNG HỒ = ÂM (&minus;)</span>
    </div>
    <div class="formula-label">Cực dễ nhớ: "Ngược kim là Dương &ndash; Thuận kim là Âm"</div>
  </div>

  <div class="box box-story">
    <div class="box-title">🛵 VÍ DỤ ĐỜI THƯỜNG: VẶN TAY GA VÀ KIM ĐỒNG HỒ</div>
    <p>Nhìn vào cái đồng hồ treo tường nhà mày: Kim phút đang ở số 12. Nếu mày dùng tay quay lùi ngược chiều kim đồng hồ đến số 9 (tức là quay $\frac{1}{4}$ vòng theo chiều dương), góc lượng giác quét được là $+90^\circ$.</p>
    <p style="margin-top:6px;">Nhưng nếu đồng hồ tự chạy bình thường từ số 12 đến số 3 (thuận chiều kim đồng hồ $\frac{1}{4}$ vòng), nó đang quay theo chiều ÂM, số đo góc lượng giác lúc này là $-90^\circ$!</p>
    <p style="margin-top:6px;">Nếu một chiếc xe máy đua chạy trên đường tròn 2 vòng rưỡi theo chiều ngược kim đồng hồ: góc quét được là $+2,5 \times 360^\circ = +900^\circ$! Góc lớn hơn $360^\circ$ hay góc âm là chuyện cực kì bình thường trong lượng giác!</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 CÔNG THỨC SỐ ĐO TỔNG QUÁT CỦA GÓC LƯỢNG GIÁC (SGK Trang 6)</div>
    <div class="formula-display">
      sđ(Ou, Ov) = &alpha; + k &times; 360&deg;  (hoặc &alpha; + k &times; 2&pi;)   (k &isin; &Zopf;)
    </div>
    <div class="formula-label">Đại lượng: &alpha; là số đo góc ban đầu; k là số vòng quay nguyên; k &isin; Z nghĩa là k có thể âm, dương hoặc bằng 0</div>
    <ul class="content-list" style="margin-top:8px;">
      <li><strong>Ý nghĩa của chữ $k$:</strong> Cứ quay thêm 1 vòng ($360^\circ$) thì lại quay về đúng vị trí cũ của tia $Ov$. Tia cuối không đổi nhưng số vòng đã tăng thêm!</li>
      <li>Ví dụ: Góc $60^\circ$, góc $60^\circ + 360^\circ = 420^\circ$, và góc $60^\circ - 360^\circ = -300^\circ$ đều có cùng tia đầu $Ou$ và tia cuối $Ov$!</li>
    </ul>
  </div>

  <!-- PHẦN 2: HỆ THỨC CHASLES -->
  <h3 class="sec-title" id="b1-chasles">2. Hệ Thức Chasles (Đi Xe Bus Chuyển Trạm)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH HỆ THỨC CHASLES CHO DÂN MẤT GỐC</div>
    <p>SGK viết: <em>"Với ba tia $Ou, Ov, Ow$ bất kì, ta có $\text{sđ}(Ou, Ov) + \text{sđ}(Ov, Ow) = \text{sđ}(Ou, Ow) + k360^\circ$."</em></p>
    <p style="margin-top:6px;">Mày nhìn có thấy quen không? Nó y xì đúc công thức cộng véc-tơ lớp 10: $\vec{AB} + \vec{BC} = \vec{AC}$!</p>
    <p style="margin-top:6px;"><strong>Hiểu theo kiểu đi xe bus:</strong> Mày đi từ bến $Ou$ sang trạm trung chuyển $Ov$, rồi từ trạm $Ov$ đi tiếp tới bến $Ow$. Tổng quãng đường góc quét được bằng đúng mày đi thẳng từ bến đầu $Ou$ tới bến cuối $Ow$ (chỉ sai khác bội số vòng quay $k360^\circ$).</p>
    <p style="margin-top:6px;"><strong>Hệ quả tính toán (chuyên dùng làm bài tập):</strong></p>
    <div class="formula-display" style="font-size:0.95rem;">
      sđ(Ou, Ov) = sđ(Ox, Ov) &minus; sđ(Ox, Ou) + k360&deg;  (như chèn gốc O: &vec;AB = &vec;OB &minus; &vec;OA)
    </div>
  </div>

  <!-- PHẦN 3: ĐỘ VÀ RADIAN -->
  <h3 class="sec-title" id="b1-radian">3. Đơn Vị Radian & Độ Dài Cung Tròn (Bảo Bối Tính Toán)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 TẠI SAO LOÀI NGƯỜI ĐẺ RA CÁI RADIAN LÀM GÌ CHO KHỔ?</div>
    <p>Độ ($^\circ$) là đơn vị người cổ đại Babylon chia vòng tròn ra 360 phần. Nhưng khi tính toán vật lý (vận tốc dài, gia tốc...), độ không phải là một con số thực, không thể cộng trừ với mét hay giây được.</p>
    <p style="margin-top:6px;">Người ta định nghĩa <strong>1 radian (viết tắt: rad)</strong>: Lấy sợi dây có chiều dài đúng bằng bán kính $R$, uốn cong đặt đè lên đường tròn. Cung tròn mà sợi dây chiếm chỗ có số đo đúng bằng <strong>1 rad</strong>!</p>
    <p style="margin-top:6px;">Chu vi cả vòng tròn là $2\pi R$. Vậy cả vòng tròn có đúng <strong>$2\pi$ radian</strong> (khoảng $2 \times 3,1416 \approx 6,28\text{ rad}$).</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 CÔNG THỨC CHUYỂN ĐỔI ĐỘ &hArr; RADIAN VÀ TÍNH ĐỘ DÀI CUNG TRÒN</div>
    <div class="formula-display">
      180&deg; = &pi; rad   &rArr;   1&deg; = <span class="fraction"><span class="num">&pi;</span><span class="den">180</span></span> rad  ;  1 rad = <span class="fraction"><span class="num">180</span><span class="den">&pi;</span></span> &deg; (&approx; 57&deg;17'45")
    </div>
    <div class="formula-display" style="margin-top:10px;color:var(--accent-green);border-color:var(--accent-green);">
      l = R &times; &alpha;   (trong đó &alpha; BẮT BUỘC tính bằng radian!)
    </div>
    <div class="formula-label">Độ dài cung tròn = Bán kính &times; Góc ở tâm (tính bằng radian)</div>
  </div>

  <div class="box box-warning">
    <div class="box-title">⚠️ BẪY TỬ THẦN TRONG BÀI KIỂM TRA GIỮA KÌ</div>
    <p><strong>CẢNH BÁO BẪY ĐỘ DÀI CUNG:</strong> Đề bài cho đường tròn bán kính $R = 10\text{ cm}$, tính độ dài cung có số đo $30^\circ$.</p>
    <p style="margin-top:6px;"><span style="color:var(--accent-red);">HỌC SINH NGU:</span> Lấy ngay $l = R \times \alpha = 10 \times 30 = 300\text{ cm}$! Điểm 0 về chỗ!</p>
    <p style="margin-top:6px;"><span style="color:var(--accent-green);">CÁCH LÀM ĐÚNG:</span> Phải đổi $30^\circ$ sang radian trước: $30^\circ = 30 \times \frac{\pi}{180} = \frac{\pi}{6}\text{ rad}$.</p>
    <p>Sau đó mới ốp công thức: $l = R \times \alpha = 10 \times \frac{\pi}{6} = \frac{5\pi}{3} \approx 5,24\text{ cm}$!</p>
  </div>

  <!-- PHẦN 4: ĐƯỜNG TRÒN LƯỢNG GIÁC & DẤU CỦA 4 GÓC PHẦN TƯ -->
  <h3 class="sec-title" id="b1-duong-tron-lg">4. Đường Tròn Lượng Giác & Dấu 4 Góc Phần Tư</h3>

  <div class="box box-theory">
    <div class="box-title">💡 MÔ HÌNH "TRÁI ĐẤT THU NHỎ" CỦA LƯỢNG GIÁC</div>
    <p>Đường tròn lượng giác là đường tròn đặt trong hệ tọa độ $Oxy$ với 3 đặc điểm bất biến:</p>
    <ul class="content-list">
      <li><strong>Tâm:</strong> Đặt ngay tại gốc tọa độ $O(0, 0)$.</li>
      <li><strong>Bán kính:</strong> $R = 1$ (siêu chuẩn mực).</li>
      <li><strong>Gốc xuất phát:</strong> Điểm $A(1, 0)$ nằm trên trục hoành bên phải.</li>
    </ul>
    <p style="margin-top:8px;"><strong>Trục tung & Trục hoành biến hình:</strong></p>
    <ul class="content-list">
      <li><strong>Trục hoành (Ox):</strong> Được gọi là <strong>TRỤC COSIN</strong> (mẹo nhớ: "Cos NẰM").</li>
      <li><strong>Trục tung (Oy):</strong> Được gọi là <strong>TRỤC SIN</strong> (mẹo nhớ: "Sin ĐỨNG").</li>
      <li>Điểm $M(x; y)$ trên đường tròn biểu diễn góc $\alpha$ thì: $\cos\alpha = x$ (chiếu xuống trục nằm) và $\sin\alpha = y$ (chiếu sang trục đứng)!</li>
      <li>$\tan\alpha = \frac{y}{x} = \frac{\sin\alpha}{\cos\alpha}$ (với $x = \cos\alpha \ne 0 \Rightarrow \alpha \ne \frac{\pi}{2} + k\pi$).</li>
      <li>$\cot\alpha = \frac{x}{y} = \frac{\cos\alpha}{\sin\alpha}$ (với $y = \sin\alpha \ne 0 \Rightarrow \alpha \ne k\pi$).</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 THẦN CHÚ XÉT DẤU 4 PHẦN TƯ: "NHẤT CẢ - NHÌ SIN - TAM TAN - TỨ COS"</div>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Góc phần tư</th>
            <th>Phạm vi góc $\alpha$</th>
            <th>$\sin\alpha$</th>
            <th>$\cos\alpha$</th>
            <th>$\tan\alpha$ & $\cot\alpha$</th>
            <th>Mẹo nhớ thần sầu</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Phần tư I</strong></td>
            <td>$0 < \alpha < \frac{\pi}{2}$ ($0^\circ - 90^\circ$)</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td><strong>NHẤT CẢ:</strong> Tất cả đều DƯƠNG!</td>
          </tr>
          <tr>
            <td><strong>Phần tư II</strong></td>
            <td>$\frac{\pi}{2} < \alpha < \pi$ ($90^\circ - 180^\circ$)</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td><strong>NHÌ SIN:</strong> Chỉ có Sin DƯƠNG, còn lại âm!</td>
          </tr>
          <tr>
            <td><strong>Phần tư III</strong></td>
            <td>$\pi < \alpha < \frac{3\pi}{2}$ ($180^\circ - 270^\circ$)</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td><strong>TAM TAN:</strong> Chỉ có Tan & Cot DƯƠNG!</td>
          </tr>
          <tr>
            <td><strong>Phần tư IV</strong></td>
            <td>$\frac{3\pi}{2} < \alpha < 2\pi$ ($270^\circ - 360^\circ$)</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td style="color:var(--accent-green);font-weight:700;">+</td>
            <td style="color:var(--accent-red);font-weight:700;">&minus;</td>
            <td><strong>TỨ COS:</strong> Chỉ có Cos DƯƠNG, còn lại âm!</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- PHẦN 5: BẢNG GÓC ĐẶC BIỆT & CÔNG THỨC CƠ BẢN -->
  <h3 class="sec-title" id="b1-cong-thuc-co-ban">5. Bảng Giá Trị Đặc Biệt & 4 Hệ Thức Cơ Bản</h3>

  <div class="box box-formula">
    <div class="box-title">📐 BẢNG GIÁ TRỊ LƯỢNG GIÁC CÁC GÓC ĐẶC BIỆT (PHẢI THUỘC LẦU LẦU)</div>
    <div class="tbl-wrap">
      <table>
        <thead>
          <tr>
            <th>Độ</th>
            <th>$0^\circ$</th>
            <th>$30^\circ$</th>
            <th>$45^\circ$</th>
            <th>$60^\circ$</th>
            <th>$90^\circ$</th>
            <th>$180^\circ$</th>
          </tr>
          <tr>
            <th>Radian</th>
            <th>$0$</th>
            <th>$\frac{\pi}{6}$</th>
            <th>$\frac{\pi}{4}$</th>
            <th>$\frac{\pi}{3}$</th>
            <th>$\frac{\pi}{2}$</th>
            <th>$\pi$</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>$\sin\alpha$</strong></td>
            <td>$0$</td>
            <td>$\frac{1}{2}$</td>
            <td>$\frac{\sqrt{2}}{2}$</td>
            <td>$\frac{\sqrt{3}}{2}$</td>
            <td>$1$</td>
            <td>$0$</td>
          </tr>
          <tr>
            <td><strong>$\cos\alpha$</strong></td>
            <td>$1$</td>
            <td>$\frac{\sqrt{3}}{2}$</td>
            <td>$\frac{\sqrt{2}}{2}$</td>
            <td>$\frac{1}{2}$</td>
            <td>$0$</td>
            <td>$-1$</td>
          </tr>
          <tr>
            <td><strong>$\tan\alpha$</strong></td>
            <td>$0$</td>
            <td>$\frac{\sqrt{3}}{3}$</td>
            <td>$1$</td>
            <td>$\sqrt{3}$</td>
            <td><em>Không XĐ</em></td>
            <td>$0$</td>
          </tr>
          <tr>
            <td><strong>$\cot\alpha$</strong></td>
            <td><em>Không XĐ</em></td>
            <td>$\sqrt{3}$</td>
            <td>$1$</td>
            <td>$\frac{\sqrt{3}}{3}$</td>
            <td>$0$</td>
            <td><em>Không XĐ</em></td>
          </tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:0.8rem;color:var(--text-muted);margin-top:6px;">💡 Mẹo nhớ dòng Sin: $\frac{\sqrt{0}}{2}, \frac{\sqrt{1}}{2}, \frac{\sqrt{2}}{2}, \frac{\sqrt{3}}{2}, \frac{\sqrt{4}}{2} = 1$. Dòng Cos viết ngược lại từ phải sang trái!</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BỘ TỨ CÔNG THỨC LƯỢNG GIÁC CƠ BẢN (DÙNG ĐẾN HẾT ĐỜI HỌC SINH)</div>
    <div class="formula-display">
      1) sin<sup>2</sup>&alpha; + cos<sup>2</sup>&alpha; = 1
    </div>
    <div class="formula-display" style="margin-top:8px;">
      2) 1 + tan<sup>2</sup>&alpha; = <span class="fraction"><span class="num">1</span><span class="den">cos<sup>2</sup>&alpha;</span></span>   (&alpha; &ne; <span class="fraction"><span class="num">&pi;</span><span class="den">2</span></span> + k&pi;)
    </div>
    <div class="formula-display" style="margin-top:8px;">
      3) 1 + cot<sup>2</sup>&alpha; = <span class="fraction"><span class="num">1</span><span class="den">sin<sup>2</sup>&alpha;</span></span>   (&alpha; &ne; k&pi;)
    </div>
    <div class="formula-display" style="margin-top:8px;">
      4) tan&alpha; &times; cot&alpha; = 1
    </div>
  </div>

  <!-- PHẦN 6: GÓC LIÊN KẾT ĐẶC BIỆT -->
  <h3 class="sec-title" id="b1-goc-lien-ket">6. Góc Liên Kết Đặc Biệt (Bài Thơ Bất Hủ Của Giới Toán Học)</h3>

  <div class="box box-formula">
    <div class="box-title">🔥 THẦN CHÚ: "COS ĐỐI &ndash; SIN BÙ &ndash; PHỤ CHÉO &ndash; HƠN KÉM PI TAN COT"</div>
    <p>Câu này có nghĩa là: <em>Thằng nào được đọc tên trong câu thần chú thì giữ nguyên dấu dương bằng nhau, những thằng còn lại bị vả dấu ÂM vào mặt!</em></p>
    
    <div class="accordion-item" style="margin-top:12px;">
      <button class="accordion-trigger open" onclick="toggleAcc(this)">
        <span>1. COS ĐỐI (Hai góc &minus;&alpha; và &alpha;)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content open">
        <div class="accordion-inner">
          <p>Chỉ có <strong>$\cos(-\alpha) = \cos\alpha$</strong> là bằng nhau!</p>
          <p style="color:var(--text-secondary);margin-top:4px;">Còn lại: $\sin(-\alpha) = -\sin\alpha$ ; $\tan(-\alpha) = -\tan\alpha$ ; $\cot(-\alpha) = -\cot\alpha$.</p>
          <p style="font-size:0.8rem;color:var(--accent-yellow);margin-top:4px;">Ví dụ: $\cos(-60^\circ) = \cos 60^\circ = 0,5$. Nhưng $\sin(-30^\circ) = -\sin 30^\circ = -0,5$.</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>2. SIN BÙ (Hai góc bù nhau có tổng bằng &pi; hay 180&deg;: &alpha; và &pi; &minus; &alpha;)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Chỉ có <strong>$\sin(\pi - \alpha) = \sin\alpha$</strong> là bằng nhau!</p>
          <p style="color:var(--text-secondary);margin-top:4px;">Còn lại ăn dấu trừ: $\cos(\pi - \alpha) = -\cos\alpha$ ; $\tan(\pi - \alpha) = -\tan\alpha$ ; $\cot(\pi - \alpha) = -\cot\alpha$.</p>
          <p style="font-size:0.8rem;color:var(--accent-yellow);margin-top:4px;">Ví dụ: $\sin(150^\circ) = \sin(180^\circ - 30^\circ) = \sin 30^\circ = 0,5$. Nhưng $\cos 150^\circ = -\cos 30^\circ = -\frac{\sqrt{3}}{2}$.</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>3. PHỤ CHÉO (Hai góc phụ nhau có tổng bằng 90&deg; hay &pi;/2: &alpha; và &pi;/2 &minus; &alpha;)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Chữ "CHÉO" nghĩa là đổi vai trò cho nhau: <strong>Sin đổi thành Cos &ndash; Tan đổi thành Cot</strong>!</p>
          <p style="color:var(--text-secondary);margin-top:4px;">$\sin(\frac{\pi}{2} - \alpha) = \cos\alpha$ ; $\cos(\frac{\pi}{2} - \alpha) = \sin\alpha$ ; $\tan(\frac{\pi}{2} - \alpha) = \cot\alpha$ ; $\cot(\frac{\pi}{2} - \alpha) = \tan\alpha$.</p>
          <p style="font-size:0.8rem;color:var(--accent-yellow);margin-top:4px;">Ví dụ: $\sin 60^\circ = \cos 30^\circ = \frac{\sqrt{3}}{2}$; $\tan 75^\circ = \cot 15^\circ$.</p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>4. HƠN KÉM PI (&alpha; và &alpha; + &pi;)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Chỉ có <strong>$\tan(\alpha + \pi) = \tan\alpha$</strong> và <strong>$\cot(\alpha + \pi) = \cot\alpha$</strong> là bằng nhau!</p>
          <p style="color:var(--text-secondary);margin-top:4px;">Sin và Cos bị vả dấu trừ: $\sin(\alpha + \pi) = -\sin\alpha$ ; $\cos(\alpha + \pi) = -\cos\alpha$.</p>
        </div>
      </div>
    </div>

  </div>

  <!-- PHẦN 7: BÀI TẬP THỰC CHIẾN STEP-BY-STEP -->
  <h3 class="sec-title" id="b1-thuc-chien">7. Thực Chiến Giải Bài Tập Mẫu Chuẩn Thi Giữa Kì (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 1: TÍNH CÁC GIÁ TRỊ LƯỢNG GIÁC KHI BIẾT 1 GIÁ TRỊ VÀ KHOẢNG GÓC</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Cho $\cos\alpha = -\frac{3}{5}$ với $\pi < \alpha < \frac{3\pi}{2}$. Tính $\sin\alpha, \tan\alpha, \cot\alpha$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Soi đề bài & phát hiện bẫy giấu mặt</strong>
          <p>Đề cho góc $\alpha \in (\pi; \frac{3\pi}{2})$. Đây là <strong>GÓC PHẦN TƯ THỨ III</strong>! Theo thần chú <em>"Tam Tan"</em>, ở góc phần tư III thì chỉ có $\tan$ và $\cot$ dương, còn <strong>$\sin\alpha$ BẮT BUỘC PHẢI ÂM</strong>. Thằng nào quên không xét dấu chỗ này là ăn trọn quả trứng ngỗng!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Chọn công thức phù hợp</strong>
          <p>Biết $\cos$, muốn tìm $\sin \Rightarrow$ Lôi ngay công thức $\sin^2\alpha + \cos^2\alpha = 1$.</p>
          <p>$\sin^2\alpha = 1 - \cos^2\alpha = 1 - \left(-\frac{3}{5}\right)^2 = 1 - \frac{9}{25} = \frac{16}{25}$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Khai căn & chọn nghiệm chuẩn</strong>
          <p>Vì $\sin^2\alpha = \frac{16}{25} \Rightarrow \sin\alpha = \pm \frac{4}{5}$.</p>
          <p>Do $\pi < \alpha < \frac{3\pi}{2}$ (góc phần tư III) nên $\sin\alpha < 0 \Rightarrow \mathbf{\sin\alpha = -\frac{4}{5}}$.</p>
          <p>Tiếp theo tính $\tan$ và $\cot$:</p>
          <p>$\tan\alpha = \frac{\sin\alpha}{\cos\alpha} = \frac{-4/5}{-3/5} = \mathbf{\frac{4}{3}}$.</p>
          <p>$\cot\alpha = \frac{1}{\tan\alpha} = \mathbf{\frac{3}{4}}$. Cả hai đều dương, hoàn toàn khớp với lý thuyết "Tam Tan"!</p>
        </div>
      </div>
    </div>
  </div>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 2: RÚT GỌN BIỂU THỨC DÙNG CUNG LIÊN KẾT ĐẶC BIỆT</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Rút gọn biểu thức $A = \sin(\pi - x) + \cos(\frac{\pi}{2} - x) + \cos(-x) + \cos(\pi + x)$.</p>
      
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem đáp án hoặc ăn chửi nếu làm ẩu!</button>
      <div class="answer-content">
        <p><strong>Mổ xẻ từng số hạng bằng 4 câu thần chú:</strong></p>
        <ul class="content-list">
          <li>1) $\sin(\pi - x)$: <em>Sin bù</em> $\Rightarrow \sin(\pi - x) = \sin x$.</li>
          <li>2) $\cos(\frac{\pi}{2} - x)$: <em>Phụ chéo</em> $\Rightarrow \cos(\frac{\pi}{2} - x) = \sin x$.</li>
          <li>3) $\cos(-x)$: <em>Cos đối</em> $\Rightarrow \cos(-x) = \cos x$.</li>
          <li>4) $\cos(\pi + x)$: <em>Hơn kém pi</em> (chỉ tan/cot giữ dấu) $\Rightarrow \cos(\pi + x) = -\cos x$.</li>
        </ul>
        <p style="margin-top:8px;"><strong>Gom tất cả lại:</strong></p>
        <p>$A = \sin x + \sin x + \cos x + (-\cos x) = \mathbf{2\sin x}$. Quá nhanh, quá nguy hiểm!</p>
      </div>
    </div>
  </div>

  <!-- PHẦN 8: TRẮC NGHIỆM ĐÁNH GIÁ 15 CÂU -->
  <div class="quiz-section" id="b1-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 1 (15 CÂU)</div>
        <div class="quiz-sub">Gồm Trắc nghiệm 4 lựa chọn, Đúng/Sai và Tự luận điền số &bull; Đạt 12/15 là đỗ!</div>
      </div>
      <div class="quiz-score-badge" id="b1-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Góc có số đo $108^\circ$ đổi sang đơn vị radian bằng bao nhiêu?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q1" value="A"> A. $\frac{\pi}{5}$ rad</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="B"> B. $\frac{3\pi}{5}$ rad</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="C"> C. $\frac{2\pi}{5}$ rad</label>
        <label class="quiz-option"><input type="radio" name="b1_q1" value="D"> D. $\frac{4\pi}{5}$ rad</label>
      </div>
      <div class="quiz-explain">Giải thích: Áp dụng công thức $\alpha = 108 \times \frac{\pi}{180} = \frac{108}{180}\pi = \frac{3\pi}{5}$ rad. Chọn B.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Một cung tròn có bán kính $R = 8\text{ cm}$ và số đo $\alpha = \frac{3\pi}{4}\text{ rad}$. Độ dài của cung tròn đó là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q2" value="A"> A. $6\pi\text{ cm}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="B"> B. $8\pi\text{ cm}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="C"> C. $12\pi\text{ cm}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q2" value="D"> D. $4\pi\text{ cm}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Độ dài cung tròn $l = R \times \alpha = 8 \times \frac{3\pi}{4} = 6\pi\text{ cm}$. Chọn A.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho góc $\alpha$ thỏa mãn $\frac{\pi}{2} < \alpha < \pi$. Khẳng định nào sau đây là ĐÚNG?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q3" value="A"> A. $\sin\alpha < 0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="B"> B. $\cos\alpha > 0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="C"> C. $\tan\alpha < 0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q3" value="D"> D. $\cot\alpha > 0$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\frac{\pi}{2} < \alpha < \pi$ là góc phần tư II. Theo thần chú "Nhì Sin", ở phần tư II chỉ có $\sin\alpha > 0$, còn $\cos\alpha < 0, \tan\alpha < 0, \cot\alpha < 0$. Do đó C đúng.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Biểu thức nào sau đây là ĐÚNG với mọi góc $\alpha$ làm cho biểu thức có nghĩa?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q4" value="A"> A. $\sin^2\alpha - \cos^2\alpha = 1$</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="B"> B. $1 + \tan^2\alpha = \frac{1}{\sin^2\alpha}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="C"> C. $\tan\alpha + \cot\alpha = 1$</label>
        <label class="quiz-option"><input type="radio" name="b1_q4" value="D"> D. $1 + \cot^2\alpha = \frac{1}{\sin^2\alpha}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hệ thức lượng giác cơ bản là $1 + \cot^2\alpha = \frac{1}{\sin^2\alpha}$. Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Giá trị của $\cos(-60^\circ) + \sin 150^\circ$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q5" value="A"> A. $0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="B"> B. $1$</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="C"> C. $\frac{\sqrt{3}}{2}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q5" value="D"> D. $-1$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos(-60^\circ) = \cos 60^\circ = \frac{1}{2}$. $\sin 150^\circ = \sin(180^\circ - 30^\circ) = \sin 30^\circ = \frac{1}{2}$. Tổng $= \frac{1}{2} + \frac{1}{2} = 1$. Chọn B.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Đơn giản biểu thức $M = \cos(\frac{\pi}{2} - x) + \sin(\pi - x)$, ta được kết quả là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q6" value="A"> A. $2\sin x$</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="B"> B. $0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="C"> C. $2\cos x$</label>
        <label class="quiz-option"><input type="radio" name="b1_q6" value="D"> D. $\sin x + \cos x$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos(\frac{\pi}{2} - x) = \sin x$ (phụ chéo). $\sin(\pi - x) = \sin x$ (sin bù). Do đó $M = \sin x + \sin x = 2\sin x$. Chọn A.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho $\sin\alpha = \frac{5}{13}$ và $\frac{\pi}{2} < \alpha < \pi$. Giá trị của $\cos\alpha$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q7" value="A"> A. $\frac{12}{13}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="B"> B. $\pm \frac{12}{13}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="C"> C. $-\frac{12}{13}$</label>
        <label class="quiz-option"><input type="radio" name="b1_q7" value="D"> D. $-\frac{8}{13}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos^2\alpha = 1 - \sin^2\alpha = 1 - \frac{25}{169} = \frac{144}{169}$. Vì $\frac{\pi}{2} < \alpha < \pi$ (phần tư II) nên $\cos\alpha < 0 \Rightarrow \cos\alpha = -\frac{12}{13}$. Chọn C.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Theo hệ thức Chasles, với ba tia $Ou, Ov, Ow$ bất kì, ta có $\text{sđ}(Ou, Ov) + \text{sđ}(Ov, Ow) =$</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b1_q8" value="A"> A. $\text{sđ}(Ow, Ou) + k2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="B"> B. $\text{sđ}(Ov, Ou) + k2\pi$</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="C"> C. $0$</label>
        <label class="quiz-option"><input type="radio" name="b1_q8" value="D"> D. $\text{sđ}(Ou, Ow) + k2\pi$</label>
      </div>
      <div class="quiz-explain">Giải thích: Hệ thức Chasles: $\text{sđ}(Ou, Ov) + \text{sđ}(Ov, Ow) = \text{sđ}(Ou, Ow) + k2\pi$ ($k \in \mathbb{Z}$). Chọn D.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Mỗi góc lượng giác gốc $O$ được xác định duy nhất bởi tia đầu $Ou$, tia cuối $Ov$ và số đo của nó. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! SGK trang 6 khẳng định: Mỗi góc lượng giác gốc O được xác định bởi tia đầu Ou, tia cuối Ov và số đo của nó.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Chiều quay cùng chiều quay của kim đồng hồ được quy ước là chiều DƯƠNG. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI BÉT! Quy ước quốc tế: Ngược chiều kim đồng hồ là chiều DƯƠNG, cùng chiều kim đồng hồ là chiều ÂM!</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Trên đường tròn lượng giác, trục hoành $Ox$ được gọi là trục cosin, trục tung $Oy$ được gọi là trục sin. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Hoành độ điểm biểu diễn là $\cos\alpha$, tung độ là $\sin\alpha$. Mẹo nhớ: Cos nằm, Sin đứng.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Giá trị của $\tan\alpha$ luôn xác định với mọi góc $\alpha \in \mathbb{R}$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! $\tan\alpha = \frac{\sin\alpha}{\cos\alpha}$, nên mẫu $\cos\alpha \ne 0 \Leftrightarrow \alpha \ne \frac{\pi}{2} + k\pi$. Tại các góc $90^\circ, 270^\circ...$ tan không xác định!</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Đẳng thức $\cos(\pi - \alpha) = -\cos\alpha$ luôn đúng với mọi góc $\alpha$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Theo thần chú "Sin bù", chỉ có $\sin(\pi - \alpha) = \sin\alpha$, còn $\cos(\pi - \alpha) = -\cos\alpha$.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Điền đáp số</div>
      <div class="quiz-q-text">Bánh xe đạp có đường kính $680\text{ mm}$ (bán kính $R = 340\text{ mm} = 0,34\text{ m}$). Nếu bánh xe quay được $5$ vòng thì quãng đường xe đi được là bao nhiêu mét? (Lấy $\pi \approx 3,1416$, làm tròn đến 2 chữ số thập phân).</div>
      <textarea placeholder="Nhập đáp số hoặc tóm tắt cách tính của bạn vào đây..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Mỗi vòng quay bánh xe quét góc $2\pi$ rad $\Rightarrow 5$ vòng quét góc $\alpha = 5 \times 2\pi = 10\pi$ rad.
        <br>&bull; Quãng đường đi được bằng độ dài cung lăn: $s = R \times \alpha = 0,34 \times 10\pi = 3,4\pi \approx 10,68\text{ m}$.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Giải thích</div>
      <div class="quiz-q-text">Giải thích ngắn gọn bằng ngôn ngữ đời thường: Tại sao nói $\sin^2\alpha + \cos^2\alpha = 1$ thực chất chính là định lý Pytago?</div>
      <textarea placeholder="Viết câu trả lời giải thích bằng tiếng người của bạn..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn dân hiểu bài:</strong>
        <br>Trên đường tròn lượng giác có bán kính $R = 1$, xét điểm $M(\cos\alpha; \sin\alpha)$ tạo với gốc $O$ và hình chiếu thành một tam giác vuông có cạnh huyền $OM = R = 1$, hai cạnh góc vuông là $|\cos\alpha|$ và $|\sin\alpha|$.
        <br>Theo Pytago: $(\text{cạnh huyền})^2 = (\text{cạnh vuông 1})^2 + (\text{cạnh vuông 2})^2 \Rightarrow 1^2 = \sin^2\alpha + \cos^2\alpha$. Đó chính là Pytago trong hình hài lượng giác!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b1')">🏆 Chấm Điểm Bài 1 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""

B2_CONTENT = r"""
<section class="lesson-section" id="bai-2">
  <div class="lesson-header">
    <div class="lesson-number">2</div>
    <div class="lesson-meta">
      <h2>BÀI 2: CÔNG THỨC LƯỢNG GIÁC</h2>
      <div class="lesson-sub">SGK Kết Nối Tri Thức &bull; Chương I &bull; Trang 16 &ndash; 21</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Công thức cộng</span>
        <span class="lesson-tag">Công thức nhân đôi</span>
        <span class="lesson-tag">Công thức hạ bậc</span>
        <span class="lesson-tag">Tích thành tổng</span>
        <span class="lesson-tag">Tổng thành tích</span>
      </div>
    </div>
  </div>

  <div class="sgk-viewer">
    <button class="sgk-btn" onclick="openSgkModal('page_07.png')">📖 Xem SGK Trang 16-17</button>
    <button class="sgk-btn" onclick="openSgkModal('page_08.png')">📖 Xem SGK Trang 18-19</button>
    <button class="sgk-btn" onclick="openSgkModal('page_09.png')">📖 Xem SGK Trang 20-21</button>
  </div>

  <!-- PHẦN 1: CÔNG THỨC CỘNG -->
  <h3 class="sec-title" id="b2-cong-thuc-cong">1. Công Thức Cộng (Nền Móng Của Mọi Biến Đổi)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: CÔNG THỨC CỘNG LÀ GÌ?</div>
    <p>Nhiều đứa mất gốc tưởng bở: $\cos(a + b) = \cos a + \cos b$. <strong>SAI BÉT NHÈ!</strong> Lượng giác không có trò nhân phân phối như đại số đâu con lạy bố!</p>
    <p style="margin-top:6px;">Muốn tách một góc tổng $(a + b)$ hay góc hiệu $(a - b)$ ra từng góc con $a$ và $b$, các cụ nhà toán học đã tìm ra bộ quy tắc chuẩn mực sau đây:</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BỘ TỨ CÔNG THỨC CỘNG & BÀI THƠ TRUYỀN MIỆNG</div>
    <div class="formula-display">
      cos(a &minus; b) = cos a &times; cos b + sin a &times; sin b<br>
      cos(a + b) = cos a &times; cos b &minus; sin a &times; sin b
    </div>
    <div class="formula-display" style="margin-top:8px;">
      sin(a + b) = sin a &times; cos b + cos a &times; sin b<br>
      sin(a &minus; b) = sin a &times; cos b &minus; cos a &times; sin b
    </div>
    <div class="formula-display" style="margin-top:8px;">
      tan(a + b) = <span class="fraction"><span class="num">tan a + tan b</span><span class="den">1 &minus; tan a &times; tan b</span></span>   ;   
      tan(a &minus; b) = <span class="fraction"><span class="num">tan a &minus; tan b</span><span class="den">1 + tan a &times; tan b</span></span>
    </div>
    <div class="formula-label">Thơ mẹo nhớ bất hủ:</div>
    <ul class="content-list" style="margin-top:8px;font-style:italic;">
      <li>"Cos thì cos cos sin sin &ndash; Dấu trừ đổi cộng, dấu cộng đổi trừ." (Cos rất bướng, dấu luôn bị đảo ngược!)</li>
      <li>"Sin thì sin cos cos sin &ndash; Dấu nào giữ nấy cho mình nhớ lâu." (Sin rất ngoan, dấu cộng vẫn là cộng, trừ vẫn là trừ!)</li>
      <li>"Tan tổng thì lấy tổng tan &ndash; Chia một trừ tích tan tan rõ ràng."</li>
    </ul>
  </div>

  <!-- PHẦN 2: CÔNG THỨC NHÂN ĐÔI & HẠ BẬC -->
  <h3 class="sec-title" id="b2-nhan-doi-ha-bac">2. Công Thức Nhân Đôi & Công Thức Hạ Bậc</h3>

  <div class="box box-theory">
    <div class="box-title">💡 NGUỒN GỐC TỰ NHIÊN: LẤY B = A TRONG CÔNG THỨC CỘNG</div>
    <p>Chẳng cần học vẹt! Nếu mày thay $b = a$ vào công thức cộng, mày sẽ tự chế ra ngay công thức nhân đôi trong 3 giây:</p>
    <p>&bull; $\sin(a + a) = \sin 2a = \sin a \cos a + \cos a \sin a = \mathbf{2\sin a \cos a}$.</p>
    <p>&bull; $\cos(a + a) = \cos 2a = \cos a \cos a - \sin a \sin a = \mathbf{\cos^2 a - \sin^2 a}$.</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BA KHUÔN MẶT CỦA COS 2A (CỰC KÌ HAY GẶP)</div>
    <div class="formula-display">
      cos 2a = cos<sup>2</sup>a &minus; sin<sup>2</sup>a = 2cos<sup>2</sup>a &minus; 1 = 1 &minus; 2sin<sup>2</sup>a
    </div>
    <div class="formula-display" style="margin-top:8px;">
      sin 2a = 2sin a &times; cos a   ;   tan 2a = <span class="fraction"><span class="num">2tan a</span><span class="den">1 &minus; tan<sup>2</sup>a</span></span>
    </div>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 CÔNG THỨC HẠ BẬC (BIẾN MŨ 2 THÀNH GÓC NHÂN ĐÔI MŨ 1)</div>
    <p>Từ $2\cos^2 a - 1 = \cos 2a$ và $1 - 2\sin^2 a = \cos 2a$, ta rút ra ngay công thức hạ bậc:</p>
    <div class="formula-display">
      cos<sup>2</sup>a = <span class="fraction"><span class="num">1 + cos 2a</span><span class="den">2</span></span>   ;   
      sin<sup>2</sup>a = <span class="fraction"><span class="num">1 &minus; cos 2a</span><span class="den">2</span></span>
    </div>
    <div class="formula-label">Mẹo nhớ phân biệt: Cos mang dấu CỘNG (+) &bull; Sin mang dấu TRỪ (&minus;)</div>
  </div>

  <!-- PHẦN 3: TÍCH THÀNH TỔNG & TỔNG THÀNH TÍCH -->
  <h3 class="sec-title" id="b2-tich-tong">3. Biến Đổi Tích Thành Tổng & Tổng Thành Tích</h3>

  <div class="box box-formula">
    <div class="box-title">📐 CÔNG THỨC BIẾN ĐỔI TÍCH THÀNH TỔNG (SGK Trang 19)</div>
    <div class="formula-display">
      cos a &times; cos b = <span class="fraction"><span class="num">1</span><span class="den">2</span></span> [cos(a &minus; b) + cos(a + b)]<br>
      sin a &times; sin b = <span class="fraction"><span class="num">1</span><span class="den">2</span></span> [cos(a &minus; b) &minus; cos(a + b)]<br>
      sin a &times; cos b = <span class="fraction"><span class="num">1</span><span class="den">2</span></span> [sin(a &minus; b) + sin(a + b)]
    </div>
    <div class="formula-label">Lưu ý: Luôn luôn đặt góc hiệu (a &minus; b) ở phía trước để không sợ góc âm!</div>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 CÔNG THỨC BIẾN ĐỔI TỔNG THÀNH TÍCH (SGK Trang 20)</div>
    <div class="formula-display">
      cos u + cos v = 2 &times; cos<span class="fraction"><span class="num">u + v</span><span class="den">2</span></span> &times; cos<span class="fraction"><span class="num">u &minus; v</span><span class="den">2</span></span><br>
      cos u &minus; cos v = &minus;2 &times; sin<span class="fraction"><span class="num">u + v</span><span class="den">2</span></span> &times; sin<span class="fraction"><span class="num">u &minus; v</span><span class="den">2</span></span><br>
      sin u + sin v = 2 &times; sin<span class="fraction"><span class="num">u + v</span><span class="den">2</span></span> &times; cos<span class="fraction"><span class="num">u &minus; v</span><span class="den">2</span></span><br>
      sin u &minus; sin v = 2 &times; cos<span class="fraction"><span class="num">u + v</span><span class="den">2</span></span> &times; sin<span class="fraction"><span class="num">u &minus; v</span><span class="den">2</span></span>
    </div>
    <div class="formula-label">Thơ mẹo nhớ kinh điển:</div>
    <ul class="content-list" style="margin-top:8px;font-style:italic;">
      <li>"Cos cộng cos bằng hai cos cos &ndash; Cos trừ cos bằng trừ hai sin sin (chú ý có dấu trừ!)"</li>
      <li>"Sin cộng sin bằng hai sin cos &ndash; Sin trừ sin bằng hai cos sin."</li>
    </ul>
  </div>

  <!-- PHẦN 4: THỰC CHIẾN BÀI 2 -->
  <h3 class="sec-title" id="b2-thuc-chien">4. Thực Chiến Giải Bài Tập Mẫu Bài 2 (Step-by-Step)</h3>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 1: TÍNH GIÁ TRỊ LƯỢNG GIÁC GÓC 75&deg; KHÔNG DÙNG MÁY TÍNH</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Không dùng máy tính, hãy tính giá trị của $\cos 75^\circ$.</p>
      
      <div class="step">
        <div class="step-num">1</div>
        <div class="step-content">
          <strong>Bước 1: Phân tích góc lạ thành tổng 2 góc đặc biệt</strong>
          <p>Góc $75^\circ$ không có trong bảng đặc biệt. Nhưng ta thấy ngay: $75^\circ = 45^\circ + 30^\circ$. Cả hai góc $45^\circ$ và $30^\circ$ đều là "người quen" trong bảng đặc biệt!</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">2</div>
        <div class="step-content">
          <strong>Bước 2: Ốp công thức cộng cos</strong>
          <p>Theo thơ: "Cos thì cos cos sin sin, dấu cộng đổi trừ":</p>
          <p>$\cos 75^\circ = \cos(45^\circ + 30^\circ) = \cos 45^\circ \cos 30^\circ - \sin 45^\circ \sin 30^\circ$.</p>
        </div>
      </div>

      <div class="step">
        <div class="step-num">3</div>
        <div class="step-content">
          <strong>Bước 3: Lắp số từ bảng đặc biệt vào</strong>
          <p>$\cos 75^\circ = \left(\frac{\sqrt{2}}{2}\right) \times \left(\frac{\sqrt{3}}{2}\right) - \left(\frac{\sqrt{2}}{2}\right) \times \left(\frac{1}{2}\right) = \frac{\sqrt{6} - \sqrt{2}}{4}$. Xong bài mẫu mực!</p>
        </div>
      </div>
    </div>
  </div>

  <div class="step-solver">
    <div class="step-solver-header">🎯 BÀI TẬP 2: RÚT GỌN BIỂU THỨC DÙNG NHÂN ĐÔI VÀ HẠ BẬC</div>
    <div class="step-solver-body">
      <p><strong>Đề bài:</strong> Rút gọn biểu thức $P = \frac{\sin 2x}{1 + \cos 2x}$.</p>
      <button class="btn-reveal" onclick="toggleAnswer(this)">🧠 Bấm vào để xem cách biến đổi đẹp như tranh vẽ!</button>
      <div class="answer-content">
        <p><strong>Tư duy chọn công thức:</strong></p>
        <p>&bull; Tử số: $\sin 2x = 2\sin x \cos x$.</p>
        <p>&bull; Mẫu số: Thấy xuất hiện số $1 + \cos 2x$. Trong 3 bộ mặt của $\cos 2x$, ta chọn mặt nào có số $-1$ để triệt tiêu số $1$ này đi! Đó chính là $\cos 2x = 2\cos^2 x - 1$.</p>
        <p>Khi đó: $1 + \cos 2x = 1 + (2\cos^2 x - 1) = 2\cos^2 x$.</p>
        <p><strong>Lắp vào biểu thức:</strong></p>
        <p>$P = \frac{2\sin x \cos x}{2\cos^2 x} = \frac{\sin x}{\cos x} = \mathbf{\tan x}$. Quá vi diệu!</p>
      </div>
    </div>
  </div>

  <!-- PHẦN 5: TRẮC NGHIỆM ĐÁNH GIÁ BÀI 2 -->
  <div class="quiz-section" id="b2-quiz">
    <div class="quiz-header">
      <div class="quiz-icon">📝</div>
      <div>
        <div class="quiz-title">BÀI TEST ĐÁNH GIÁ ĐỘ HIỂU BÀI 2 (15 CÂU)</div>
        <div class="quiz-sub">Đầy đủ công thức cộng, nhân đôi, biến đổi tích - tổng &bull; Đạt 12/15 là xuất sắc!</div>
      </div>
      <div class="quiz-score-badge" id="b2-score">Điểm: 0/15</div>
    </div>

    <!-- CÂU 1 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 1 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Khẳng định nào sau đây là công thức cộng ĐÚNG?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q1" value="A"> A. $\cos(a + b) = \cos a \cos b - \sin a \sin b$</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="B"> B. $\cos(a + b) = \cos a \cos b + \sin a \sin b$</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="C"> C. $\sin(a + b) = \sin a \cos b - \cos a \sin b$</label>
        <label class="quiz-option"><input type="radio" name="b2_q1" value="D"> D. $\cos(a - b) = \sin a \sin b - \cos a \cos b$</label>
      </div>
      <div class="quiz-explain">Giải thích: Cos thì dấu cộng đổi thành dấu trừ: $\cos(a + b) = \cos a \cos b - \sin a \sin b$. Chọn A.</div>
    </div>

    <!-- CÂU 2 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 2 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Công thức nhân đôi nào sau đây là SAI?</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q2" value="A"> A. $\sin 2a = 2\sin a \cos a$</label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="B"> B. $\cos 2a = 2\cos^2 a - 1$</label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="C"> C. $\cos 2a = 2\sin^2 a - 1$</label>
        <label class="quiz-option"><input type="radio" name="b2_q2" value="D"> D. $\cos 2a = 1 - 2\sin^2 a$</label>
      </div>
      <div class="quiz-explain">Giải thích: $\cos 2a = 1 - 2\sin^2 a$ chứ không phải $2\sin^2 a - 1$. Chọn C.</div>
    </div>

    <!-- CÂU 3 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 3 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Biểu thức $\sin a \cos b + \cos a \sin b$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q3" value="A"> A. $\sin(a - b)$</label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="B"> B. $\sin(a + b)$</label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="C"> C. $\cos(a + b)$</label>
        <label class="quiz-option"><input type="radio" name="b2_q3" value="D"> D. $\cos(a - b)$</label>
      </div>
      <div class="quiz-explain">Giải thích: Đây chính là vế phải của công thức cộng sin: $\sin(a + b) = \sin a \cos b + \cos a \sin b$. Chọn B.</div>
    </div>

    <!-- CÂU 4 -->
    <div class="quiz-q" data-type="mc" data-ans="D">
      <div class="quiz-q-num">Câu 4 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Công thức hạ bậc của $\cos^2 a$ là:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q4" value="A"> A. $\frac{1 - \cos 2a}{2}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="B"> B. $\frac{1 + \sin 2a}{2}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="C"> C. $1 - \cos 2a$</label>
        <label class="quiz-option"><input type="radio" name="b2_q4" value="D"> D. $\frac{1 + \cos 2a}{2}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Cos mang dấu CỘNG: $\cos^2 a = \frac{1 + \cos 2a}{2}$. Chọn D.</div>
    </div>

    <!-- CÂU 5 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 5 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Biến đổi $\cos 5x + \cos 3x$ thành tích ta được:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q5" value="A"> A. $2\cos 4x \cos x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="B"> B. $2\sin 4x \sin x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="C"> C. $-2\sin 4x \sin x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q5" value="D"> D. $2\cos 4x \sin x$</label>
      </div>
      <div class="quiz-explain">Giải thích: Cos cộng cos bằng hai cos cos: $\cos 5x + \cos 3x = 2\cos(\frac{5x+3x}{2})\cos(\frac{5x-3x}{2}) = 2\cos 4x \cos x$. Chọn A.</div>
    </div>

    <!-- CÂU 6 -->
    <div class="quiz-q" data-type="mc" data-ans="C">
      <div class="quiz-q-num">Câu 6 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Biến đổi $\cos 7x - \cos 3x$ thành tích ta được:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q6" value="A"> A. $2\sin 5x \sin 2x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="B"> B. $-2\cos 5x \cos 2x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="C"> C. $-2\sin 5x \sin 2x$</label>
        <label class="quiz-option"><input type="radio" name="b2_q6" value="D"> D. $2\cos 5x \sin 2x$</label>
      </div>
      <div class="quiz-explain">Giải thích: "Cos trừ cos bằng trừ hai sin sin": $\cos 7x - \cos 3x = -2\sin(\frac{7x+3x}{2})\sin(\frac{7x-3x}{2}) = -2\sin 5x \sin 2x$. Chọn C.</div>
    </div>

    <!-- CÂU 7 -->
    <div class="quiz-q" data-type="mc" data-ans="B">
      <div class="quiz-q-num">Câu 7 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Cho $\sin a = \frac{3}{5}$ với $0 < a < \frac{\pi}{2}$. Giá trị của $\sin 2a$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q7" value="A"> A. $\frac{12}{25}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="B"> B. $\frac{24}{25}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="C"> C. $\frac{7}{25}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q7" value="D"> D. $-\frac{24}{25}$</label>
      </div>
      <div class="quiz-explain">Giải thích: Vì $0 < a < \frac{\pi}{2}$ nên $\cos a = \sqrt{1 - (3/5)^2} = \frac{4}{5}$. Do đó $\sin 2a = 2\sin a \cos a = 2 \times \frac{3}{5} \times \frac{4}{5} = \frac{24}{25}$. Chọn B.</div>
    </div>

    <!-- CÂU 8 -->
    <div class="quiz-q" data-type="mc" data-ans="A">
      <div class="quiz-q-num">Câu 8 &bull; Trắc nghiệm 4 lựa chọn</div>
      <div class="quiz-q-text">Giá trị của biểu thức $P = \cos 75^\circ \cos 15^\circ$ bằng:</div>
      <div class="quiz-options">
        <label class="quiz-option"><input type="radio" name="b2_q8" value="A"> A. $\frac{1}{4}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="B"> B. $\frac{1}{2}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="C"> C. $\frac{\sqrt{3}}{4}$</label>
        <label class="quiz-option"><input type="radio" name="b2_q8" value="D"> D. $\frac{1}{8}$</label>
      </div>
      <div class="quiz-explain">Giải thích: $P = \frac{1}{2}[\cos(75^\circ - 15^\circ) + \cos(75^\circ + 15^\circ)] = \frac{1}{2}[\cos 60^\circ + \cos 90^\circ] = \frac{1}{2}[\frac{1}{2} + 0] = \frac{1}{4}$. Chọn A.</div>
    </div>

    <!-- CÂU 9: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 9 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Đẳng thức $\sin(a + b) = \sin a + \sin b$ đúng với mọi số thực $a, b$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI NGU! Tuyệt đối không được phân phối sin vào tổng góc. Ví dụ $a=b=30^\circ$: $\sin 60^\circ = \frac{\sqrt{3}}{2}$, trong khi $\sin 30^\circ + \sin 30^\circ = 1 \ne \frac{\sqrt{3}}{2}$.</div>
    </div>

    <!-- CÂU 10: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 10 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Đẳng thức $\cos 2a = \cos^2 a - \sin^2 a$ luôn đúng với mọi góc $a$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Đây chính là công thức nhân đôi cơ bản của hàm cosin.</div>
    </div>

    <!-- CÂU 11: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 11 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Đẳng thức $\sin x + \cos x = \sqrt{2}\sin(x + \frac{\pi}{4})$ đúng với mọi số thực $x$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Khai triển $\sqrt{2}\sin(x + \frac{\pi}{4}) = \sqrt{2}(\sin x \cos\frac{\pi}{4} + \cos x \sin\frac{\pi}{4}) = \sqrt{2}(\frac{\sqrt{2}}{2}\sin x + \frac{\sqrt{2}}{2}\cos x) = \sin x + \cos x$.</div>
    </div>

    <!-- CÂU 12: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="F">
      <div class="quiz-q-num">Câu 12 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Biểu thức $\sin a \sin b = \frac{1}{2}[\cos(a - b) + \cos(a + b)]$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: SAI! Ở giữa phải là dấu TRỪ: $\sin a \sin b = \frac{1}{2}[\cos(a - b) - \cos(a + b)]$. Dấu cộng là của $\cos a \cos b$!</div>
    </div>

    <!-- CÂU 13: ĐÚNG SAI -->
    <div class="quiz-q" data-type="tf" data-ans="T">
      <div class="quiz-q-num">Câu 13 &bull; Câu hỏi Đúng / Sai</div>
      <div class="quiz-q-text">Nếu $\cos 2a = 0$ thì $\sin^2 a = \frac{1}{2}$. Đúng hay Sai?</div>
      <div class="tf-options">
        <button class="tf-btn" onclick="selectTF(this, 'T')">Đúng</button>
        <button class="tf-btn" onclick="selectTF(this, 'F')">Sai</button>
      </div>
      <div class="quiz-explain">Giải thích: ĐÚNG! Hạ bậc: $\sin^2 a = \frac{1 - \cos 2a}{2} = \frac{1 - 0}{2} = \frac{1}{2}$.</div>
    </div>

    <!-- CÂU 14: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 14 &bull; Tự luận / Tính toán</div>
      <div class="quiz-q-text">Rút gọn biểu thức $T = \frac{\sin 4x + \sin 2x}{\cos 4x + \cos 2x}$. Nêu rõ công thức bạn sử dụng và kết quả cuối cùng.</div>
      <textarea placeholder="Trình bày các bước biến đổi của bạn..."></textarea>
      <div class="sample-answer">
        <strong>Đáp án chuẩn:</strong>
        <br>&bull; Tử số: $\sin 4x + \sin 2x = 2\sin(\frac{4x+2x}{2})\cos(\frac{4x-2x}{2}) = 2\sin 3x \cos x$.
        <br>&bull; Mẫu số: $\cos 4x + \cos 2x = 2\cos(\frac{4x+2x}{2})\cos(\frac{4x-2x}{2}) = 2\cos 3x \cos x$.
        <br>&bull; Chia cả tử và mẫu cho $2\cos x$, ta được: $T = \frac{2\sin 3x \cos x}{2\cos 3x \cos x} = \frac{\sin 3x}{\cos 3x} = \mathbf{\tan 3x}$.
      </div>
    </div>

    <!-- CÂU 15: TỰ LUẬN -->
    <div class="quiz-q quiz-essay">
      <div class="quiz-q-num">Câu 15 &bull; Tự luận / Ứng dụng</div>
      <div class="quiz-q-text">Giải thích tại sao trong kỹ thuật âm thanh điện thoại, khi phát ra hai nốt nhạc $f_1$ và $f_2$, âm thanh kết hợp lại tạo thành hiện tượng "phách" (biến thiên biên độ) dựa vào công thức lượng giác nào?</div>
      <textarea placeholder="Giải thích dựa trên công thức lượng giác lớp 11..."></textarea>
      <div class="sample-answer">
        <strong>Giải thích chuẩn vật lý & lượng giác:</strong>
        <br>Âm thanh kết hợp là tổng hai sóng âm: $y = \sin(2\pi f_1 t) + \sin(2\pi f_2 t)$.
        <br>Theo công thức biến đổi tổng thành tích: $\sin u + \sin v = 2\cos(\frac{u-v}{2})\sin(\frac{u+v}{2})$, ta được:
        <br>$y = 2\cos(\pi(f_1 - f_2)t) \times \sin(\pi(f_1 + f_2)t)$.
        <br>Trong đó phần $2\cos(\pi(f_1 - f_2)t)$ đóng vai trò là biên độ biến thiên chậm theo thời gian với tần số phách $f_1 - f_2$, tạo ra tiếng ngân rung trầm bổng đặc trưng của âm thanh điện thoại!
      </div>
    </div>

    <button class="quiz-submit-btn" onclick="gradeQuiz('b2')">🏆 Chấm Điểm Bài 2 & Xem Phân Tích Chi Tiết</button>
  </div>
</section>
"""
