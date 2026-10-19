# -*- coding: utf-8 -*-
"""
data_b0_lop10.py - TẦNG 0: BẢO BỐI LỚP 10 ĐỂ SỐNG SÓT QUA TOÁN 11
Được thiết kế riêng cho học sinh mất gốc:
- Băm nát toàn bộ kiến thức nền tảng lớp 10 mà lớp 11 dùng hàng ngày.
- Không lan man ngoài rìa, chỉ tập trung đúng những thứ xuất hiện trong kiểm tra và thi giữa kì.
"""

B0_LOP10_CONTENT = r"""
<section class="lesson-section" id="tang-0">
  <div class="lesson-header">
    <div class="lesson-number">0</div>
    <div class="lesson-meta">
      <h2>TẦNG 0: BẢO BỐI LỚP 10 CỨU MẠNG DÂN MẤT GỐC</h2>
      <div class="lesson-sub">Nền tảng sống còn &bull; Bắt buộc phải thông suốt trước khi bước vào Toán 11</div>
      <div class="lesson-tags">
        <span class="lesson-tag">Tam giác vuông</span>
        <span class="lesson-tag">Định lý Sin - Cosin</span>
        <span class="lesson-tag">Đường tròn đơn vị</span>
        <span class="lesson-tag">Đường trung bình</span>
        <span class="lesson-tag">Định lý Thales</span>
      </div>
    </div>
  </div>

  <!-- LỜI TÂM SỰ CỦA GIA SƯ -->
  <div class="box box-story">
    <div class="box-title">🗣️ LỜI NÓI THẬT CỦA ÔNG ANH GIA SƯ</div>
    <p>Chào người anh em! Nếu mày đang mở cuốn Toán 11 ra và thấy hoa mắt chóng mặt với mớ <em>"cung lượng giác, góc alpha, radian, mặt phẳng song song"</em>, thì đừng hoảng. Mày không dốt, chỉ là mày bị <strong>đứt gãy nền móng lớp 10</strong> mà thôi!</p>
    <p style="margin-top:8px;">Toán 11 không sinh ra từ hư không. Mọi bài lượng giác lớp 11 đều cắm rễ từ hệ thức lượng lớp 10. Mọi bài hình học không gian 11 đều dựa trên định lý Thales và đường trung bình lớp 10. Ở Tầng 0 này, tao sẽ lôi đầu đúng 5 món bảo bối lớp 10 mà các thầy cô mặc định là mày đã biết, băm nát ra bằng tiếng người để mày nhai gọn trong 15 phút. Đọc xong phần này, bảo đảm mày tự tin vào lớp 11 không sợ bố con thằng nào!</p>
  </div>

  <!-- PHẦN 1: HỆ THỨC LƯỢNG TAM GIÁC VUÔNG -->
  <h3 class="sec-title" id="b0-tam-giac-vuong">1. Hệ Thức Lượng Tam Giác Vuông (Thần Chú Bất Hủ)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: SIN, COS, TAN, COT LÀ CÁI QUÁI GÌ?</div>
    <p>Hồi cấp 2, sách viết hàn lâm: <em>"Tỉ số giữa cạnh đối và cạnh huyền..."</em> nghe nhức hết cả đầu. Hiểu nôm na thế này:</p>
    <p style="margin-top:6px;">Trong một cái tam giác vuông, mày đứng ở một góc nhọn bất kì (gọi tên nó là góc $\alpha$ đi). Từ chỗ mày đứng nhìn ra xung quanh sẽ có đúng 3 cạnh:</p>
    <ul class="content-list">
      <li><strong>Cạnh huyền:</strong> Cạnh dài nhất, luôn nằm đối diện với góc vuông $90^\circ$ (nhìn phát thấy ngay).</li>
      <li><strong>Cạnh đối:</strong> Cái cạnh nằm đối diện mặt mày, mày bắn cung một phát là trúng nó.</li>
      <li><strong>Cạnh kề:</strong> Cái cạnh nằm sát ngay nách mày (dính liền với góc mày đang đứng, trừ cạnh huyền ra).</li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 BÀI THƠ THẦN CHÚ LỚP 10 (ĐỪNG BAO GIỜ QUÊN)</div>
    <div class="formula-display">
      <span style="color:var(--accent-blue-light);">Sin Đi Học</span> &bull; 
      <span style="color:var(--accent-yellow);">Cos Khóc Cười</span> &bull; 
      <span style="color:var(--accent-green);">Tan Đoàn Kết</span> &bull; 
      <span style="color:var(--accent-orange);">Cot Kết Đoàn</span>
    </div>
    <div class="formula-label">Quy tắc vàng chuyển hóa thành phân số</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));gap:12px;margin-top:14px;">
      <div style="background:var(--bg-secondary);padding:10px;border-radius:var(--radius-sm);text-align:center;">
        <strong>$\sin\alpha$ = <span class="fraction"><span class="num">ĐỐI</span><span class="den">HYỀN</span></span></strong>
        <div style="font-size:0.75rem;color:var(--text-muted);margin-top:4px;">(Đi Học: Đ / H)</div>
      </div>
      <div style="background:var(--bg-secondary);padding:10px;border-radius:var(--radius-sm);text-align:center;">
        <strong>$\cos\alpha$ = <span class="fraction"><span class="num">KỀ</span><span class="den">HYỀN</span></span></strong>
        <div style="font-size:0.75rem;color:var(--text-muted);margin-top:4px;">(Khóc Cười: K / H)</div>
      </div>
      <div style="background:var(--bg-secondary);padding:10px;border-radius:var(--radius-sm);text-align:center;">
        <strong>$\tan\alpha$ = <span class="fraction"><span class="num">ĐỐI</span><span class="den">KỀ</span></span></strong>
        <div style="font-size:0.75rem;color:var(--text-muted);margin-top:4px;">(Đoàn Kết: Đ / K)</div>
      </div>
      <div style="background:var(--bg-secondary);padding:10px;border-radius:var(--radius-sm);text-align:center;">
        <strong>$\cot\alpha$ = <span class="fraction"><span class="num">KỀ</span><span class="den">ĐỐI</span></span></strong>
        <div style="font-size:0.75rem;color:var(--text-muted);margin-top:4px;">(Kết Đoàn: K / Đ)</div>
      </div>
    </div>
  </div>

  <div class="box box-warning">
    <div class="box-title">⚠️ BẪY SAI NGU KINH ĐIỂN CỦA HỌC SINH MẤT GỐC</div>
    <p><strong>Sai lầm 1:</strong> Tam giác không vuông mà cũng đè $\sin = \text{đối} / \text{huyền}$ ra tính! Nhớ kĩ: 4 câu thần chú này <em>CHỈ ĐƯỢC PHÉP DÙNG</em> khi tam giác đó có góc $90^\circ$.</p>
    <p style="margin-top:6px;"><strong>Sai lầm 2:</strong> Nhầm lẫn giữa $\tan$ và $\cot$. Hãy nhớ: $\tan\alpha \times \cot\alpha = 1$, hai thằng này là nghịch đảo của nhau. Thằng này ngửa thì thằng kia úp!</p>
    <p style="margin-top:6px;"><strong>Hệ thức Pytago thần thánh:</strong> $(\text{Huyền})^2 = (\text{Đối})^2 + (\text{Kề})^2$. Từ đây suy ra ngay công thức cốt lõi lớp 11: $\sin^2\alpha + \cos^2\alpha = 1$.</p>
  </div>

  <!-- PHẦN 2: ĐỊNH LÝ COSIN VÀ SIN TRONG TAM GIÁC THƯỜNG -->
  <h3 class="sec-title" id="b0-dinh-ly-cosin-sin">2. Tam Giác Thường: Định Lý Cosin và Định Lý Sin</h3>

  <div class="box box-theory">
    <div class="box-title">💡 NỖI ĐAU TAM GIÁC THƯỜNG & SỰ RA ĐỜI CỦA ĐỊNH LÝ COSIN</div>
    <p>Nếu tam giác méo mó không có góc vuông thì Pytago "phế võ công". Lúc này các nhà toán học chế ra <strong>Định lý Cosin</strong> &ndash; thực chất chính là Pytago nhưng có thêm một cái "đuôi hãm phanh" phía sau để bù trừ cho độ méo của góc!</p>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 ĐỊNH LÝ COSIN (TÍNH CẠNH KHI BIẾT 2 CẠNH VÀ GÓC KẸP GIỮA)</div>
    <div class="formula-display">
      a<sup>2</sup> = b<sup>2</sup> + c<sup>2</sup> &minus; 2bc &times; cos A
    </div>
    <div class="formula-label">Quy tắc: Cạnh đối diện bình phương = Tổng bình phương 2 cạnh kề &minus; 2 lần tích 2 cạnh kề nhân cos góc kẹp giữa</div>
    <ul class="content-list" style="margin-top:10px;">
      <li>Tương tự: $b^2 = a^2 + c^2 - 2ac \cos B$</li>
      <li>Tương tự: $c^2 = a^2 + b^2 - 2ab \cos C$</li>
      <li><strong>Hệ quả tính góc (dùng cực nhiều khi giải tam giác):</strong>
        <br>$\cos A = \frac{b^2 + c^2 - a^2}{2bc}$ (Tổng bình phương 2 cạnh kề trừ bình phương cạnh đối, chia 2 lần tích 2 cạnh kề).
      </li>
    </ul>
  </div>

  <div class="box box-formula">
    <div class="box-title">📐 ĐỊNH LÝ SIN (TỈ SỐ ĐỒNG ĐỀU VỚI BÁN KÍNH ĐƯỜNG TRÒN NGOẠI TIẾP R)</div>
    <div class="formula-display">
      <span class="fraction"><span class="num">a</span><span class="den">sin A</span></span> = 
      <span class="fraction"><span class="num">b</span><span class="den">sin B</span></span> = 
      <span class="fraction"><span class="num">c</span><span class="den">sin C</span></span> = 2R
    </div>
    <div class="formula-label">Cứ lấy 1 cạnh chia cho sin của góc đối diện nó thì tỉ số luôn bằng đường kính đường tròn ngoại tiếp (2R)</div>
  </div>

  <div class="box box-story">
    <div class="box-title">🥩 VÍ DỤ ĐỜI THƯỜNG: BẮN BI TRÊN BÀN BIDA</div>
    <p>Mày đặt bi trắng tại điểm $A$, bi đỏ tại $B$, bi vàng tại $C$. Mày đo được khoảng cách $AB = 40\text{ cm}$, $AC = 60\text{ cm}$ và góc tạo bởi hai đường ngắm là $\widehat{A} = 60^\circ$. Đố mày khoảng cách từ bi đỏ đến bi vàng ($BC = a$) là bao nhiêu?</p>
    <p style="margin-top:6px;"><strong>Ốp công thức Cosin ngay:</strong></p>
    <p>$a^2 = 40^2 + 60^2 - 2 \times 40 \times 60 \times \cos 60^\circ$</p>
    <p>$a^2 = 1600 + 3600 - 4800 \times 0,5 = 5200 - 2400 = 2800 \Rightarrow a = \sqrt{2800} \approx 52,9\text{ cm}$. Xong phim trong một nốt nhạc!</p>
  </div>

  <!-- PHẦN 3: NỬA ĐƯỜNG TRÒN ĐƠN VỊ & GÓC TÙ -->
  <h3 class="sec-title" id="b0-duong-tron-don-vi">3. Nửa Đường Tròn Đơn Vị Lớp 10 (Gốc Rễ Của Bài 1 Lớp 11)</h3>

  <div class="box box-theory">
    <div class="box-title">💡 DỊCH SANG TIẾNG NGƯỜI: TẠI SAO COS GÓC TÙ LẠI BỊ ÂM?</div>
    <p>Hồi lớp 9, mày chỉ học góc nhọn ($0^\circ$ đến $90^\circ$) nên độ dài cạnh luôn dương. Nhưng lên lớp 10, người ta gắn góc vào một cái compa quay trên mặt phẳng tọa độ $Oxy$ với bán kính $R = 1$:</p>
    <ul class="content-list">
      <li>Điểm $M(x; y)$ chạy trên nửa đường tròn nằm phía trên trục hoành.</li>
      <li>Hoành độ $x$ chính là giá trị của $\cos\alpha$.</li>
      <li>Tung độ $y$ chính là giá trị của $\sin\alpha$.</li>
    </ul>
    <p style="margin-top:8px;"><strong>Hệ quả chấn động:</strong></p>
    <ul class="content-list">
      <li>Khi góc $\alpha$ <strong>nhọn</strong> ($0^\circ < \alpha < 90^\circ$): Điểm $M$ nằm bên phải trục tung $\Rightarrow x > 0 \Rightarrow \mathbf{\cos\alpha > 0}$. Cả $\sin\alpha > 0$.</li>
      <li>Khi góc $\alpha$ <strong>tù</strong> ($90^\circ < \alpha < 180^\circ$): Điểm $M$ dạt sang bên trái trục tung $\Rightarrow x < 0 \Rightarrow \mathbf{\cos\alpha < 0}$ (bị âm lòi ra!). Trong khi đó nó vẫn ở trên trục hoành nên $\sin\alpha > 0$.</li>
      <li><strong>Hai góc bù nhau ($\alpha$ và $180^\circ - \alpha$):</strong> $\sin(180^\circ - \alpha) = \sin\alpha$ (bằng nhau), nhưng $\cos(180^\circ - \alpha) = -\cos\alpha$ (bị đổi dấu âm!).</li>
    </ul>
  </div>

  <!-- PHẦN 4: VŨ KHÍ HÌNH HỌC PHẲNG DÙNG TRONG HÌNH KHÔNG GIAN -->
  <h3 class="sec-title" id="b0-hinh-hoc-phang">4. "Vũ Khí Lớp 10" Chuyên Dùng Cho Hình Không Gian Lớp 11</h3>

  <div class="box box-recall">
    <div class="box-title">🔥 3 ĐỊNH LÝ HÌNH HỌC PHẲNG MÀ BÀI TẬP HÌNH 11 NÀO CŨNG ÉP MÀY DÙNG</div>
    
    <div class="accordion-item" style="margin-top:10px;">
      <button class="accordion-trigger open" onclick="toggleAcc(this)">
        <span>1. Đường Trung Bình (Vũ khí tối thượng chứng minh song song)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content open">
        <div class="accordion-inner">
          <p><strong>Trong tam giác:</strong> Đường nối trung điểm hai cạnh bên thì song song với cạnh đáy và có độ dài bằng <strong>MỘT NỬA</strong> cạnh đáy!</p>
          <div class="formula-display" style="font-size:0.95rem;">
            M là trung điểm AB, N là trung điểm AC &rArr; MN &parallel; BC và MN = &frac12; BC
          </div>
          <p style="color:var(--accent-yellow);font-size:0.85rem;margin-top:6px;"><em>Lên lớp 11: Cứ thấy đề bài cho trung điểm 2 cạnh bên của hình chóp hay tứ diện, 99% là phải lôi đường trung bình ra để chứng minh đường thẳng song song với mặt phẳng!</em></p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>2. Trọng Tâm Tam Giác (Quy tắc tỉ lệ 2/3 thần thánh)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p>Trọng tâm $G$ là giao điểm của 3 đường trung tuyến trong tam giác. Nó có tính chất chia mỗi đường trung tuyến thành 3 phần bằng nhau:</p>
          <div class="formula-display" style="font-size:0.95rem;">
            <span class="fraction"><span class="num">AG</span><span class="den">AM</span></span> = <span class="fraction"><span class="num">2</span><span class="den">3</span></span> ; 
            <span class="fraction"><span class="num">GM</span><span class="den">AM</span></span> = <span class="fraction"><span class="num">1</span><span class="den">3</span></span> ; 
            <span class="fraction"><span class="num">AG</span><span class="den">GM</span></span> = 2
          </div>
          <p style="color:var(--accent-yellow);font-size:0.85rem;margin-top:6px;"><em>Lên lớp 11: Đề thi giữa kì cực thích cho 2 trọng tâm $G_1, G_2$ của hai tam giác. Khi đó ta dùng tỉ lệ $2/3$ của định lý Thales để suy ra $G_1 G_2$ song song với một đường thẳng khác!</em></p>
        </div>
      </div>
    </div>

    <div class="accordion-item">
      <button class="accordion-trigger" onclick="toggleAcc(this)">
        <span>3. Định Lý Thales (Thuận & Đảo)</span>
        <span class="acc-icon">▼</span>
      </button>
      <div class="accordion-content">
        <div class="accordion-inner">
          <p><strong>Thales thuận:</strong> Nếu một đường thẳng song song với một cạnh của tam giác và cắt hai cạnh còn lại thì nó định ra trên hai cạnh đó những đoạn thẳng tương ứng tỉ lệ.</p>
          <p style="margin-top:6px;"><strong>Thales đảo (Chuyên dùng để chứng minh song song):</strong></p>
          <div class="formula-display" style="font-size:0.95rem;">
            Nếu <span class="fraction"><span class="num">AM</span><span class="den">AB</span></span> = <span class="fraction"><span class="num">AN</span><span class="den">AC</span></span> &rArr; MN &parallel; BC
          </div>
          <p style="color:var(--accent-green);font-size:0.85rem;margin-top:6px;"><em>Đây là kim chỉ nam để giải các câu lấy điểm 8-9 trong bài thi giữa kì Hình học không gian!</em></p>
        </div>
      </div>
    </div>

  </div>

  <!-- BẢNG TỔNG KẾT TẦNG 0 -->
  <h3 class="sec-title">5. Bảng So Sánh & Chốt Hạ Kiến Thức Tầng 0</h3>
  <div class="tbl-wrap">
    <table>
      <thead>
        <tr>
          <th>Tên Bảo Bối Lớp 10</th>
          <th>Công Thức / Bản Chất</th>
          <th>Ứng Dụng Sống Còn Lên Lớp 11</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Sin, Cos, Tan, Cot</strong></td>
          <td>Đi học &ndash; Khóc cười &ndash; Đoàn kết &ndash; Kết đoàn</td>
          <td>Dựng đường tròn lượng giác Bài 1, tính giá trị góc</td>
        </tr>
        <tr>
          <td><strong>$\sin^2\alpha + \cos^2\alpha = 1$</strong></td>
          <td>Bắt nguồn từ Pytago tam giác vuông</td>
          <td>Biến đổi mọi biểu thức lượng giác Bài 1, 2, 4</td>
        </tr>
        <tr>
          <td><strong>Định lý Cosin & Sin</strong></td>
          <td>$a^2 = b^2 + c^2 - 2bc\cos A$; $\frac{a}{\sin A} = 2R$</td>
          <td>Giải các bài toán thực tế đo đạc, tam giác méo</td>
        </tr>
        <tr>
          <td><strong>Đường trung bình</strong></td>
          <td>Nối trung điểm 2 cạnh, song song và bằng $\frac{1}{2}$ đáy</td>
          <td>Chứng minh đường thẳng song song mặt phẳng (Bài 11, 12)</td>
        </tr>
        <tr>
          <td><strong>Trọng tâm $G$ (tỉ lệ 2/3)</strong></td>
          <td>$AG / AM = 2/3$</td>
          <td>Kết hợp định lý Thales đảo để chứng minh song song</td>
        </tr>
      </tbody>
    </table>
  </div>
</section>
"""
