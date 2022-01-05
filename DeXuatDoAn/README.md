# **Dự đoán người có đội mũ bảo hiểm hay không?**

## Bài toán dùng ở đâu và để làm gì:
- Sử dụng cho các thiết bị giám sát của công an giao thông (điện thoại, máy ảnh), giúp phát hiện đối tượng vi phạm không đội nón bảo hiểm dễ dàng hơn.
- Giup cảnh sát giao thông có thể kiểm soát người vi phạm tốt hơn ở những cung đường có nhiều xe lưu thông mà mắt thường không thể kiểm soát nổi 

## Bài toán gồm:
-input: ảnh người tham gia giao thông
-output: ảnh kèm theo bounding box và thông tin nhãn (có đội nón bảo hiểm hoặc không đội nón bảo hiểm

## Mô tả dữ liệu:
- Data bao gồm các ảnh về người tham gia giao thông (chủ yếu là xe gắn máy, xe đạp điện, những phương tiện cần đội nón bảo hiểm) được chụp tầm thấp như vd.

![image](https://user-images.githubusercontent.com/76487372/147796584-904b3e38-133a-4541-a63e-74dec872afe6.png)
 
- Dự kiếm 2000 ảnh tỉ lệ train/test 80/20.
- Cách thu thập data: sử dụng điện thoại cá nhân, các thành viên tự chụp ở địa phương mình.
## Mô hình.

- Đánh giá bounding box thông qua chỉ số mAP (mean anverage precision)
 
![image](https://user-images.githubusercontent.com/76487372/147796634-8585636b-07b0-4c67-adf3-733348eabcb4.png)

![image](https://user-images.githubusercontent.com/76487372/147796639-78ceaae1-d8b2-4740-a3e4-87ab1cea5d53.png)

 
Precision: Thể hiện sự chuẩn xác của việc phát hiện các điểm Positive. Số này càng cao thì model nhận các điểm Positive càng chuẩn
 
 ![image](https://user-images.githubusercontent.com/76487372/147796652-00b3510a-d4ea-4d9b-b390-d4fce1e7bb2f.png)

Recall:  Thể hiện khả năng phát hiện tất cả các postivie, tỷ lệ này càng cao thì cho thấy khả năng bỏ sót các điểm Positive là thấp

![image](https://user-images.githubusercontent.com/76487372/147796654-eea52198-f567-4a53-8193-4735c6a14657.png)

F1 score: Là số dung hòa Recall và Precision giúp ta có căn cứ để lựa chọn model. F1 càng cao càng tốt.

Đối với bounding box việc xác địnhTP, FN,FP như sau:
 
 ![image](https://user-images.githubusercontent.com/76487372/147796658-af4e7999-ee15-466a-af63-d967573898e0.png)

Chọn một ngưỡng X.
Các tiêu chí được dùng để đánh giá:
– Đối tượng được nhận dạng đúng, với tỉ lệ IoU > X (True positive : TP)
– Đối tượng được nhận dạng sai với tỉ lệ IoU < X (False positive : FP)
– Đối tượng không được nhận dạng (False negative: FN)
mAP :Trung bình AP của từ mỗi class
Đánh giá qua Average precision (AP).

![image](https://user-images.githubusercontent.com/76487372/147798473-e8291731-01d3-473e-9b10-8c9e42df196f.png)
