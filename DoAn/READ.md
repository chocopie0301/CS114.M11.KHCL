
# **Dự đoán người có đội mũ bảo hiểm hay không?**

## Bài toán dùng ở đâu và để làm gì:
- Sử dụng cho các thiết bị giám sát của công an giao thông (điện thoại, máy ảnh), giúp phát hiện đối tượng vi phạm không đội nón bảo hiểm dễ dàng hơn.
- Giup cảnh sát giao thông có thể kiểm soát người vi phạm tốt hơn ở những cung đường có nhiều xe lưu thông mà mắt thường không thể kiểm soát nổi 

## Bài toán gồm:
-input: ảnh người tham gia giao thông
-output: ảnh kèm theo bounding box và thông tin nhãn (có đội nón bảo hiểm hoặc không đội nón bảo hiểm

## Mô tả dữ liệu:
- Data bao gồm các ảnh về người tham gia giao thông (chủ yếu là xe gắn máy, xe đạp điện, những phương tiện cần đội nón bảo hiểm) được chụp tầm thấp như vd.
 
- Dự kiếm 2000 ảnh tỉ lệ train/test 80/20.
- Cách thu thập data: sử dụng điện thoại cá nhân, các thành viên tự chụp ở địa phương mình.
## Mô hình.
- Đánh giá nhãn thông qua các chỉ số f1-score
- Đánh giá bounding box thông qua chỉ số mAP (mean anverage precision)
 

 
Precision: Thể hiện sự chuẩn xác của việc phát hiện các điểm Positive. Số này càng cao thì model nhận các điểm Positive càng chuẩn
 
Recall:  Thể hiện khả năng phát hiện tất cả các postivie, tỷ lệ này càng cao thì cho thấy khả năng bỏ sót các điểm Positive là thấp
 
F1 score: Là số dung hòa Recall và Precision giúp ta có căn cứ để lựa chọn model. F1 càng cao càng tốt .
Đối với bounding box việc xác địnhTP, FN,FP như sau:
 
Chọn một ngưỡng X.
Các tiêu chí được dùng để đánh giá:
– Đối tượng được nhận dạng đúng với tỉ lệ IOU> X (True positive : TP)
– Đối tượng được nhận dạng sai với tỉ lệ IOU < X (False positive : FP)
– Đối tượng không được nhận dạng (False negative: FN)
mAP :Trung bình AP của từ mỗi class
AP: Trung bình n Precision của mỗi n Recall.




# ---------------------------------------------------------------------------------------------------------------------

# **Dự đoán khoảng cách phòng dịch covid của mọi người di chuyển trong nơi công cộng?**

## Bài toán dùng ở đâu và để làm gì:

Nếu ta là một công dân biết tuân thủ hoặc chưa tuân thủ trước đó và muốn tuân thủ ngay khuyến cáo 5K trong đó có điều thứ 3 "khoảng cách", thì khi 
thấy 1 nhóm người khả nghi thì ta có thể rút chiếc thoại ra chụp lại hình ảnh, "phân tích" xem nhóm người đó đã tuân thủ đúng khoảng cách phòng dịch
chưa? Nếu chưa thì báo chính quyền để họ đóng thuế cho ý thức. 

"Phân tích" việc tuân thủ của nhóm người đó tuân thủ hay chưa qua hình ảnh là công việc của nhóm em trong đồ án này bằng việc xây dựng dữ liệu cho máy học
để máy dự đoán.

## Bài toán gồm:
input: ảnh 1 nhóm người 

output: đã tuân thủ khoảng cách phòng dịch hay chưa

## Mô tả dữ liệu:

Dữ liệu sẽ được thành viên trong nhóm chụp.

Dự kiến 1600 ảnh (có thể nhiều hơn tùy thuộc vào tình hình dịch ở quê của từng bạn vào những ngày tới)

Dữ liệu chia làm 3 tập train/dev/test với tỉ lệ: 60/20/20

## Mô hình: 
- Đánh giá qua độ chính xác.
- Mục tiêu dự kiến: Xác định được mô hình tốt nhất, kết quả dự đoán khớp với kích thước bàn chân thực tế, giá trị accuracy >=0.8 .



##---------------------------------------------------------------------------------------------------------------------------------------------
# **DỰ ĐOÁN KÍCH THƯỚC BÀN CHÂN CỦA KHÁCH HÀNG CÓ NHU CẦU MUA GIÀY**

## Nhóm TTP:

1. Nguyễn Thành Trung - 19522432
2. Trần Hồ Thiên Phước - 19522057

## Bài toán dùng ở đâu và để làm gì:
- Bài toán tích hợp trên một app có chức năng chụp/quét và nên thuộc quyền sở hữu bởi 1 shop giày.
- Đối tượng sử dụng: những người mới mua giày nhưng chưa biết size giày của bản thân hoặc người có nhu cầu mua giày custom size nhưng lại ở quá xa shop, những người bị ảnh hưởng việc đi lại bởi dịch covid. (Đối tượng hướng đến chủ yếu có kinh tế thuộc diện trung bình khá/ các bạn trẻ, học sinh, sinh viên nên giày được đề cập trong đồ án không được sản xuất bằng các chất liệu xịn để có giá thành phổ thông nhất đến với khách hàng (400k vnd < x < 900k vnd)).
- Bài toán nhằm thay thế việc đo đạc thủ công, đảm bảo giày được mua đúng kích thước khách hàng yêu cầu và tăng sự đa dạng size giày của shop, giúp việc mua bán diễn ra nhanh hơn thông qua dữ liệu thu thập được từ những khách hàng đã sử dụng đủ lớn.

## Bài toán gồm:

1. Input: Một tấm ảnh bàn chân.
2. Output: Kết quả là kích thước của bàn chân.

## Mô tả dữ liệu:

- Dự kiến ~1200 ảnh do chính các thành viên chụp.
- Thông số: chiều dài bàn chân (ảnh chụp hướng lòng trong bàn chân: tính từ ngón chân dài nhất đến gót chân), chiều rộng bàn chân (ảnh chụp từ trên xuống và chính diện bàn chân), chiều cao tính từ phần chân chạm đất đến mu bàn chân và mắt cá chân (ảnh chụp hướng vào máng ngoài bàn chân).

Ví dụ:

![image](https://user-images.githubusercontent.com/76487372/147374872-098a8803-adab-4dac-a44e-8504484ca8c1.png)
                            Hình 1. Ảnh chụp hướng lòng trong bàn chân


![image](https://user-images.githubusercontent.com/76487372/147374916-c5adc8f4-fd58-47c0-ad71-66d21be76cad.png)
                            Hình 2. Ảnh chụp từ trên xuống và chính diện bàn chân


![image](https://user-images.githubusercontent.com/76487372/147374947-ad2148e7-78f0-44e9-aead-62d82e5bdfd8.png)
                            Hình 3. Chiều cao bàn chân.


- Dữ liệu được chia theo tỉ lệ 70%-train, 15%-dev, 15%-test.

## Mô hình:

- Đánh giá qua độ chính xác, F1-score.
- Mục tiêu dự kiến: Xác định được mô hình tốt nhất, kết quả dự đoán khớp với kích thước bàn chân thực tế, giá trị accuracy và F1-score đều >=0.8 .



