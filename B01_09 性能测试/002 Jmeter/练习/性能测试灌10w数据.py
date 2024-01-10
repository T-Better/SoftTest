import pymysql
conn = pymysql.connect(host="192.168.146.130", user="litemall", password="litemall123456", database="litemall", port=3306)
cursor = conn.cursor()
goods_sql = """
INSERT INTO `litemall_goods` (`id`, `goods_sn`, `name`, `category_id`, `brand_id`, `gallery`,
`keywords`, `brief`, `is_on_sale`, `sort_order`, `pic_url`, `share_url`, `is_new`, `is_hot`, `unit`,
`counter_price`, `retail_price`, `detail`, `add_time`, `update_time`, `deleted`)
VALUES ('{}', '{}', '小米手机-{}', '1008016', '1001000', '[\"http://182.92.81.159:8080/wx/storage/fetch/0b5lpf15ee8c6o10vkd8.jpg\",\
"http://182.92.81.159:8080/wx/storage/fetch/ykaptr4vntbofoi9l2f5.jpg\",\"http://182.92.81.159:8080/wx/storage/fetch/u5zc8sp2t4f9y9uw
n179.jpg\"]',
'手机,Android', '小米10 双模5G 骁龙865 1亿像素8K电影相机', '1', '100', 'http://182.92.81.159:8080/wx/storage/fetch/re5jul69plklzusso97
t.png', '', '1', '0', '个', '100.00', '99.00', '<p>小米10 双模5G 骁龙865 1亿像素8K电影相机 对称式立体声 8GB+256GB 冰海蓝 拍照智能游戏手机
！！！！！！！！！！</p>',
'2020-03-11 14:19:50', '2020-03-26 14:55:58', '0');"""

goods_attr_sql = """
INSERT INTO `litemall_goods_attribute` (`goods_id`, `attribute`, `value`, `add_time`, `update_time`, `deleted`)
VALUES
('{}', '产地', '中国山东', '2018-10-26 21:27:13', '2018-10-26 21:27:13', '0'),
('{}', '尺寸', '200*230cm/ 220*240cm', '2018-10-26 21:27:13', '2018-10-26 21:27:13', '0'),
('{}', '颜色', '条纹绿格', '2018-10-26 21:27:13', '2018-10-26 21:27:13', '0'),
('{}', '执行标准', 'GB/T 22844-2009', '2018-10-26 21:27:13', '2018-10-26 21:27:13', '0');
"""
goods_product_sql = """
INSERT INTO `litemall_goods_product` (`goods_id`, `specifications`, `price`, `number`, `url`, `add_time`, `update_time`, `deleted`)
VALUES ('{}', '[\"标准\"]', '999.00', '1000', 'http://182.92.81.159:8080/wx/storage/fetch/o4531ja3h9sgq5ib32f4.jpg', '2020-03-11 14:
19:50', '2020-03-11 14:19:50', '0');
"""
goods_spec_sql = """
INSERT INTO `litemall_goods_specification` (`goods_id`, `specification`, `value`, `pic_url`, `add_time`, `update_time`, `deleted`)
VALUES ('{}', '规格', '标准', '', '2020-03-11 14:19:50', '2020-03-11 14:19:50', '0');
"""
goods_id_start = 200000
for i in range(100000):
    # 商品
    goods_id = goods_id_start + i
    print("i={} goods_id={}".format(i, goods_id))
    sql = goods_sql.format(goods_id, goods_id, goods_id)
    cursor.execute(sql)
    # 商品参数
    sql = goods_attr_sql.format(goods_id, goods_id, goods_id, goods_id)
    cursor.execute(sql)
    # 商品货品
    sql = goods_product_sql.format(goods_id)
    cursor.execute(sql)
    # 商品规格表
    sql = goods_spec_sql.format(goods_id)
    cursor.execute(sql)
    conn.commit()
cursor.close()
conn.close()