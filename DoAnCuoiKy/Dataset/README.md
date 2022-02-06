# **Mô tả thông tin về cách xây dựng và sử dụng dataset**

1. Thu thập dữ liệu
- Đầu tiên, nhóm đi hỏi xin các tạp hóa, các quán xá gần nhà nhưng không được câu trả lời mong muốn. Lúc này, nhóm em đã xin những người quen ở xa. Sau khi nhận được các video trích xuất từ camera giám sát, nhóm đã thực hiện chuyển các video về thành ảnh rồi lọc lấy các ảnh đúng tiêu chí được nêu ở Phần 2 mục 1 bằng ứng dụng DVDVideoSoft Free Studio.  Vì ở xa nên nhóm cũng chỉ mô tả qua lời nói dẫn đến số video được người thân gửi chỉ lọc ra được 150 ảnh qua 3 videos dài trung bình khoảng 40 phút nhưng mất tới 4 ngày để thu thập. Nhận thấy cách thu thập này không hiệu quả về mặt thời gian nên nhóm có sử dụng thêm 600 ảnh từ cuộc thi Data-Centric AI Competition được tổ chức vào cuối năm 2021 vừa rồi bởi FPT. 
- Nhóm em cải thiện số lượng ảnh trong bộ dữ liệu bằng cách thu thập các video có trên Youtube với các từ khóa tìm kiếm như ‘camera thu ngân’, ‘demo camera’.. và chuyển đổi các video sang ảnh. Từ khoảng 20 video dài ngắn khác nhau nhóm thu được 497 ảnh, tuy nhiên việc chuyển đổi ảnh này cũng không có tính đa dạng về background, màu sắc, độ sáng tối trong ảnh vì số hình ảnh được chọn chỉ diễn ra tại cùng một thời điểm cho một  video.
![image](https://user-images.githubusercontent.com/76487372/152640372-0695c42c-722a-4873-8223-80ee97ba55a5.png)

- Vì thế nhóm quyết định tăng tính đa dạng dữ liệu của bộ dữ liệu bằng cách thu thập thêm ảnh trên Google qua việc search với từ khóa “wear mask in public places”, rồi lọc lấy các ảnh phù hợp.
![image](https://user-images.githubusercontent.com/76487372/152640374-b8545be4-94e2-4492-a124-331d13967c3d.png)

- Nhờ đó, số lượng ảnh cuối cùng nhóm thu thập được là 1461 ảnh.

2. Xây dựng dữ liệu trên Roboflow

2.1. Tiêu chí thu thập thập ảnh

Ảnh được lấy có các tiêu chí sau:

-	Là ảnh chụp từ góc cao.
-	Ảnh chụp nơi cộng đồng.
-	Ảnh thấy được rõ mặt, hoặc ảnh có thể xác định được chân mày hoặc mắt từ vùng trán xuống tới cằm.
-	Ảnh bị che khuất một phần nhưng thấy được các phần còn lại của vùng từ chân mày xuống tới cằm hoặc miệng.

Ảnh không được lấy có các đặc điểm sau:

-	Ảnh bị mờ, không xác định được rõ bộ phận nào của mặt chỉ thấy được màu da.
-	Ảnh có tất cả người đứng gần nhưng chỉ chụp được phần trán tới mũi.
-	Ảnh chụp người đứng quá xa.

2.2. Quy tắc kẻ bounding box và gán nhãn

Vì trong ảnh có nhiều người nên việc kẻ bounding box và gán nhãn cũng dựa trên nhiều tiêu chí ảnh được/ không được lấy, gồm các quy tắc như sau:

-	Bounding box kẻ từ vùng đỉnh trán xuống tới cằm, không lấy phần tai ở những khuôn mặt thấy rõ.
-	Ảnh người bị che khuất một phần nhưng phần còn lại vẫn thấy được như tiêu chí ở phần lấy ảnh thì ta sẽ kẻ bounding box phần thấy được đó.

![image](https://user-images.githubusercontent.com/76487372/152640324-d6248fa0-c8aa-4ac2-8787-126bdcd0a966.png)

-	Những khuôn mặt được chụp từ góc nghiêng, khuất đi vùng mặt trước thì nhóm sẽ xét nếu vùng tai được nhìn rõ thì sẽ kẻ bounding box, không thì bỏ qua. 
	![image](https://user-images.githubusercontent.com/76487372/152640336-5c2f78da-1574-495d-bdc0-f7d638c46b3b.png)
	
-	Trường hợp khuôn mặt được chụp thấy được tất cả các bộ phận trên khuôn mặt nhưng bị mờ/ không thấy rõ thì nhóm sẽ xác định vùng chân mày, mắt có thể phân biệt với màu sắc của da không, nếu có thì thực hiện kẻ bounding box, không thì bỏ qua.
-	Không kẻ bounding box với các khuôn mặt không thấy rõ bộ phận chân mày hoặc mắt, các khuôn mặt quá nhỏ.
-	Việc gán nhãn cho từng bounding box nhóm đã thống nhất 0 cho nhãn không đeo và 2 cho nhãn đeo.

2.3. Chia dữ liệu

Để thực hiện phân chia dữ liệu hiệu quả, tránh tình trạng overfit trên bộ dữ liệu có số lượng chưa được nhiều, chưa được quá đa dạng và kiểm tra được model có tốt hay không, cùng với đó nhóm sử dụng mô hình YOLOv5 để huấn luyện nên tập validation là quan trọng trong việc đánh giá. Vì vậy, nhóm chỉ dùng 66 ảnh cho việc test, được lưu riêng ở trên drive và không tải lên Roboflow, 1395 ảnh nhóm tải lên Roboflow chia theo tỉ lệ 80/20 cho train/val. Sau khi Roboflow chia ngẫu nhiên ảnh, nhóm thực hiện lọc thủ công lấy những ảnh có đặc trưng riêng, những ảnh không có tính trùng lặp trong cả bộ dữ liệu với các ảnh còn lại sang tập validation, rồi chuyển những ảnh gần giống nhau sang tập train.

![image](https://user-images.githubusercontent.com/76487372/152640545-19d20523-b2d5-4aa6-bd9a-745795e56a2a.png)

2.4. Tiền xử lý dữ liệu

- Dữ liệu sau khi được chia trên Roboflow sẽ tiếp tục đến bước tiền xử lý dữ liệu bằng cách chuyển các ảnh về kích thước 414x416. Để đồng bộ tất cả ảnh, tránh tình trạng nhiễu hay lỗi. Việc chuyển ảnh về kích thước nhỏ hơn cũng giúp quá trình huấn luyện mô hình diễn ra nhanh hơn. 
![image](https://user-images.githubusercontent.com/76487372/152640562-e0a9026b-9fb4-4735-8e5e-d3016e413b36.png)
- Nhóm có áp dụng thêm lựa chọn ‘Auto-Orient’ trong bước tiền xử lý. Với ‘Auto-Orient’, các bounding box sẽ luôn được định hướng theo đối tượng đã được kẻ bounding box trước đó khi ảnh bị xoay. ‘Auto-Orient’ khá hữu ích cho việc tăng cường dữ liệu sử dụng phép xoay.
2.5. Tăng cường dữ liệu
- Với Augmentations trên Roboflow, các thông số như hình 16 là lựa chọn mang lại kết quả tốt nhất trong tất cả các lần lựa chọn các thông số một cách ngẫu nhiên của nhóm, vì vậy kết quả của việc tăng cường còn mang khá nhiều tính chủ quan.
•	Flip- Horizontal: Lật ngang các đối tượng trong ảnh.
•	90o Rotate- Clockwise, Counter-Clockwise: Xoay ảnh sang ngang. Giúp mô hình không bị nhầm lẫn với hướng của máy ảnh.
→ Flip, 90o Rotate: đa dạng vị trí các bounding box.
•	Hue: thay đổi màu sắc trong khoảng -60o đến +60o của ảnh.
•	Saturation: thay đổi cường độ màu sắc trong khoảng -30% đến +30%.
•	Brightness: thay đổi độ sáng-tối của nền ảnh trong khoảng -40% đến 40%.
→ Hue, Saturation, Brightness: đa dạng màu sắc, cường độ màu sắc của các ảnh và độ sáng-tối nền ảnh.

![image](https://user-images.githubusercontent.com/76487372/152640608-15e7d4e3-1ee5-4fb0-bea6-9ff54b8e69c0.png)

 Hình 16. Tăng cường dữ liệu trên Roboflow.
 
Với việc sử dụng cách tăng cường dữ liệu như trên, kết quả biểu đồ Heatmap nhóm nhận được sau cùng đã cải thiện rõ rệt:
![image](https://user-images.githubusercontent.com/76487372/152640615-5c6cd99a-cea3-43d5-9c05-3172bd8d29fa.png) 
(a)

![image](https://user-images.githubusercontent.com/76487372/152640662-fe9f1c36-788a-4b21-b589-fec099bb3e47.png)
(b)

![image](https://user-images.githubusercontent.com/76487372/152640675-36b93d85-dc39-4469-a9db-1042c8fa78d8.png) 
(c)

		Hình 17.  Các Heatmap của bộ dữ liệu đã được tăng cường.


