-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- 主机： 127.0.0.1:3306
-- 生成日期： 2023-06-17 09:16:54
-- 服务器版本： 8.0.29
-- PHP 版本： 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `drug_data`
--

-- --------------------------------------------------------

--
-- 表的结构 `app_admin`
--

DROP TABLE IF EXISTS `app_admin`;
CREATE TABLE IF NOT EXISTS `app_admin` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_admin`
--

INSERT INTO `app_admin` (`id`, `username`, `password`) VALUES
(1, 'admin', 'admin');

-- --------------------------------------------------------

--
-- 表的结构 `app_chuku`
--

DROP TABLE IF EXISTS `app_chuku`;
CREATE TABLE IF NOT EXISTS `app_chuku` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `drug_name` varchar(32) NOT NULL,
  `out_money` decimal(10,2) NOT NULL,
  `out_number` int DEFAULT NULL,
  `out_time` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_chuku`
--

INSERT INTO `app_chuku` (`id`, `drug_name`, `out_money`, `out_number`, `out_time`) VALUES
(1, '速效救心丸', '335.00', 10, '2023-01-02'),
(2, '速效救心丸', '335.00', 10, '2023-01-02'),
(3, '速效救心丸', '670.00', 20, '2023-02-02'),
(4, '速效救心丸', '160.00', 5, '2023-03-02'),
(5, '速效救心丸', '670.00', 20, '2023-04-02'),
(6, '速效救心丸', '335.00', 10, '2023-05-02'),
(7, '速效救心丸', '335.00', 10, '2023-06-02'),
(8, '速效救心丸', '335.00', 10, '2023-07-02'),
(9, '速效救心丸', '1005.00', 30, '2023-08-02'),
(10, '速效救心丸', '335.00', 10, '2023-09-02'),
(11, '速效救心丸', '670.00', 20, '2023-10-02'),
(12, '速效救心丸', '335.00', 10, '2023-11-02'),
(13, '速效救心丸', '335.00', 10, '2023-12-02'),
(14, '速效救心丸', '335.00', 10, '2024-01-02'),
(15, '速效救心丸', '670.00', 20, '2025-02-02'),
(16, '速效救心丸', '160.00', 5, '2025-03-02'),
(17, '速效救心丸', '670.00', 20, '2024-04-02'),
(18, '速效救心丸', '335.00', 10, '2024-05-02'),
(19, '速效救心丸', '335.00', 10, '2024-06-02'),
(20, '速效救心丸', '335.00', 10, '2024-07-02'),
(21, '速效救心丸', '1005.00', 30, '2024-08-02'),
(22, '速效救心丸', '335.00', 10, '2024-09-02'),
(23, '速效救心丸', '670.00', 20, '2024-10-02'),
(24, '速效救心丸', '335.00', 10, '2024-11-02'),
(25, '速效救心丸', '335.00', 10, '2024-12-02'),
(26, '速效救心丸', '335.00', 10, '2025-01-02'),
(27, '速效救心丸', '670.00', 20, '2025-02-02'),
(28, '速效救心丸', '160.00', 5, '2025-03-02'),
(29, '速效救心丸', '670.00', 20, '2025-04-02'),
(30, '速效救心丸', '1005.00', 30, '2025-05-02'),
(31, '速效救心丸', '335.00', 10, '2025-06-02'),
(32, '速效救心丸', '335.00', 10, '2025-07-02'),
(33, '速效救心丸', '1005.00', 30, '2025-08-02'),
(34, '速效救心丸', '335.00', 10, '2025-09-02'),
(35, '速效救心丸', '670.00', 20, '2025-10-02'),
(36, '速效救心丸', '335.00', 10, '2025-11-02'),
(37, '速效救心丸', '670.00', 20, '2025-12-02'),
(38, '藿香正气水', '500.00', 100, '2023-01-01'),
(39, '藿香正气水', '500.00', 100, '2023-01-01'),
(40, '藿香正气水', '50.00', 10, '2023-02-01'),
(41, '藿香正气水', '250.00', 50, '2023-03-01'),
(42, '藿香正气水', '300.00', 60, '2023-04-01'),
(43, '藿香正气水', '50.00', 10, '2023-05-01'),
(44, '藿香正气水', '50.00', 10, '2023-06-01'),
(45, '藿香正气水', '200.00', 40, '2023-07-01'),
(46, '藿香正气水', '150.00', 30, '2023-08-01'),
(47, '藿香正气水', '50.00', 10, '2023-09-01'),
(48, '藿香正气水', '50.00', 10, '2023-10-01'),
(49, '藿香正气水', '50.00', 10, '2023-11-01'),
(50, '藿香正气水', '50.00', 10, '2023-12-01'),
(51, '藿香正气水', '50.00', 10, '2024-01-01'),
(52, '藿香正气水', '500.00', 100, '2024-02-01'),
(53, '藿香正气水', '350.00', 70, '2024-03-01'),
(54, '藿香正气水', '400.00', 80, '2024-04-01'),
(55, '藿香正气水', '50.00', 10, '2024-05-01'),
(56, '藿香正气水', '50.00', 10, '2024-06-01'),
(57, '藿香正气水', '100.00', 20, '2024-07-01'),
(58, '藿香正气水', '100.00', 20, '2024-08-01'),
(59, '藿香正气水', '100.00', 20, '2024-09-01'),
(60, '藿香正气水', '500.00', 100, '2024-10-01'),
(61, '藿香正气水', '450.00', 90, '2024-11-01'),
(62, '藿香正气水', '100.00', 20, '2024-12-01'),
(63, '藿香正气水', '200.00', 40, '2025-01-01'),
(64, '藿香正气水', '100.00', 20, '2025-02-01'),
(65, '藿香正气水', '500.00', 100, '2025-03-01'),
(66, '藿香正气水', '250.00', 50, '2025-04-01'),
(67, '藿香正气水', '250.00', 50, '2025-05-01'),
(68, '藿香正气水', '500.00', 100, '2025-06-01'),
(69, '藿香正气水', '325.00', 65, '2025-07-01'),
(70, '藿香正气水', '275.00', 55, '2025-08-01'),
(71, '藿香正气水', '50.00', 10, '2025-09-01'),
(72, '藿香正气水', '350.00', 70, '2025-10-01'),
(73, '藿香正气水', '50.00', 10, '2025-11-01'),
(74, '藿香正气水', '225.00', 45, '2025-12-01'),
(75, '抗病毒颗粒', '350.00', 10, '2023-01-03'),
(76, '抗病毒颗粒', '350.00', 10, '2023-01-03'),
(77, '抗病毒颗粒', '3500.00', 100, '2023-02-03'),
(78, '抗病毒颗粒', '1750.00', 50, '2023-03-03'),
(79, '抗病毒颗粒', '2800.00', 80, '2023-04-03'),
(80, '抗病毒颗粒', '1400.00', 40, '2023-05-03'),
(81, '抗病毒颗粒', '350.00', 10, '2023-06-03'),
(82, '抗病毒颗粒', '1400.00', 40, '2023-07-03'),
(83, '抗病毒颗粒', '2800.00', 80, '2023-08-03'),
(84, '抗病毒颗粒', '1050.00', 30, '2023-09-03'),
(85, '抗病毒颗粒', '1050.00', 30, '2023-10-03'),
(86, '抗病毒颗粒', '2800.00', 80, '2023-11-03'),
(87, '抗病毒颗粒', '1750.00', 50, '2023-12-03'),
(88, '阿司匹林散', '3500.00', 50, '2023-01-12'),
(89, '阿司匹林散', '2100.00', 30, '2023-02-11'),
(90, '阿司匹林散', '680.00', 10, '2023-03-09'),
(91, '阿司匹林散', '680.00', 10, '2023-04-13'),
(92, '阿司匹林散', '2800.00', 40, '2023-05-17'),
(93, '阿司匹林散', '1400.00', 20, '2023-06-08'),
(94, '阿司匹林散', '2100.00', 30, '2023-07-12'),
(95, '阿司匹林散', '3500.00', 50, '2023-08-16'),
(96, '阿司匹林散', '4200.00', 60, '2023-09-08'),
(97, '阿司匹林散', '2100.00', 30, '2023-10-12'),
(98, '阿司匹林散', '680.00', 10, '2023-11-10'),
(99, '阿司匹林散', '3500.00', 50, '2023-12-15'),
(100, '复方酮康唑乳膏', '1500.00', 50, '2023-01-01'),
(101, '复方酮康唑乳膏', '1500.00', 50, '2023-02-01'),
(102, '复方酮康唑乳膏', '900.00', 30, '2023-03-01'),
(103, '复方酮康唑乳膏', '1500.00', 50, '2023-04-01'),
(104, '复方酮康唑乳膏', '1800.00', 60, '2023-05-12'),
(105, '复方酮康唑乳膏', '1200.00', 40, '2023-06-01'),
(106, '复方酮康唑乳膏', '1500.00', 50, '2023-07-01'),
(107, '复方酮康唑乳膏', '600.00', 20, '2023-08-04'),
(108, '复方酮康唑乳膏', '1200.00', 40, '2023-09-01'),
(109, '复方酮康唑乳膏', '2400.00', 80, '2023-10-01'),
(110, '复方酮康唑乳膏', '900.00', 30, '2023-11-01'),
(111, '复方酮康唑乳膏', '1800.00', 60, '2023-12-01'),
(112, '藿香正气水', '50.00', 10, '2023-05-25'),
(113, '藿香正气水', '1000.00', 100, '2023-05-30'),
(114, '速效救心丸', '1000.00', 20, '2023-06-25');

-- --------------------------------------------------------

--
-- 表的结构 `app_drug`
--

DROP TABLE IF EXISTS `app_drug`;
CREATE TABLE IF NOT EXISTS `app_drug` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `drugname` varchar(32) NOT NULL,
  `drugjixing` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '剂型',
  `money` decimal(10,2) NOT NULL,
  `number` int NOT NULL COMMENT '数量',
  `drugspe` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '规格',
  `produce` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '生产企业',
  `insure` smallint NOT NULL COMMENT '保险类型',
  `drugrat` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '批准文号',
  `drugant` smallint NOT NULL COMMENT '抗菌类型',
  `drugnid` varchar(64) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL COMMENT '类型编码',
  `drugkey` smallint NOT NULL COMMENT '重点关注药品',
  `drugun` smallint NOT NULL COMMENT '一致性检验',
  `drugcate` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL COMMENT '药品分类',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=117 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_drug`
--

INSERT INTO `app_drug` (`id`, `drugname`, `drugjixing`, `money`, `number`, `drugspe`, `produce`, `insure`, `drugrat`, `drugant`, `drugnid`, `drugkey`, `drugun`, `drugcate`) VALUES
(2, '维C银翘片', '片剂', '8.00', 600, '12片/板', '西安正大制药有限公司', 1, '国药准字Z61020112', 1, '86902533001090', 2, 1, '中药'),
(3, '左氧氟沙星片', '片剂', '15.00', 500, '0.5g', '湖北多瑞药业有限公司', 2, '国药准字H20066387', 1, '86906652000194', 2, 1, '化学药品'),
(4, '吲哚美辛片', '片剂', '10.00', 1000, '25mg', '上海信谊九福药业有限公司', 1, '国药准字H31021016', 2, '86900802000232', 2, 1, '化学药品'),
(5, '复方磺胺甲噁唑片', '片剂', '22.00', 400, '0.4g', '山东端信堂大禹药业有限公司', 1, '国药准字H37020805', 1, '86904128000068', 2, 1, '化学药品'),
(6, '呋喃唑酮片', '片剂', '23.00', 430, '0.1g', '山西三晋药业有限公司', 1, '国药准字H14021356', 1, '86902926000549', 2, 1, '化学药品'),
(7, '格列吡嗪片', '片剂', '15.00', 560, '5mg', '江苏平光制药(焦作)有限公司', 1, '国药准字H20057658', 1, '86903120000205', 2, 1, '化学药品'),
(8, '安乃近片', '片剂', '10.00', 666, '0.5g', '通化白山药业股份有限公司', 1, '国药准字H22021378', 1, '86903556000022', 2, 1, '化学药品'),
(9, '对乙酰氨基酚片', '片剂', '30.00', 350, '0.3g', '河南科伦药业有限公司', 1, '国药准字H41022308', 1, '86903063000300', 2, 1, '化学药品'),
(10, '卡马西平片', '片剂', '30.00', 333, '0.1g', '常州康普药业有限公司', 3, '国药准字H32021277', 1, '86901375000971', 2, 1, '化学药品'),
(11, '头孢羟氨苄胶囊', '胶囊剂', '36.00', 420, '0.125g', '湖南中和制药有限公司', 2, '国药准字H43020044', 1, '86905005000331', 2, 1, '化学药品'),
(12, '维生素E软胶囊', '胶囊剂', '50.00', 150, '5mg', '南京海鲸药业股份有限公司', 2, '国药准字H32024177', 1, '86901564000119', 2, 2, '化学药品'),
(13, '复方蒲芩胶囊', '胶囊剂', '40.00', 190, '0.24g', '吉林巨仁堂药业股份有限公司', 1, '国药准字Z20050679', 1, '86903384000515', 1, 2, '中药'),
(14, '清火胶囊', '胶囊剂', '24.00', 320, '0.5g', '江西药都仁和制药有限公司', 4, '国药准字Z20080476', 2, '86905378001157', 2, 2, '中药'),
(15, '羚羊感冒胶囊', '胶囊剂', '38.00', 310, '0.42g', '北京亚东生物制药有限公司', 2, '国药准字Z20033203', 2, '86900200000490', 2, 2, '中药'),
(16, '益肺化痰胶囊', '胶囊剂', '45.00', 250, '0.3g', '甘肃河西制药有限责任公司', 4, '国药准字B20020460', 2, '86905858001943', 2, 1, '中药'),
(17, '诺氟沙星胶囊', '胶囊剂', '10.00', 345, '0.1g', '陕西博森生物制药股份集团有限公司', 3, '国药准字H61021346', 1, '86902428000054', 1, 1, '化学药品'),
(18, '维生素A软胶囊', '胶囊剂', '9.00', 666, '2.5g', '南京海鲸药业股份有限公司', 4, '国药准字H32021210', 1, '86901564000195', 2, 1, '化学药品'),
(19, '黄柏胶囊', '胶囊剂', '25.00', 269, '0.33g', '江西沃华济顺医药有限公司', 4, '国药准字Z20043042', 2, '86903358000694', 2, 2, '中药'),
(20, '阿莫西林胶囊', '胶囊剂', '8.00', 469, '0.125g', '福州海王福药制药有限公司', 2, '国药准字H35020305', 3, '86904827000024', 2, 1, '化学药品'),
(21, '葡萄糖注射液', '注射剂', '6.00', 432, '20ml:10g', '济川药业集团有限公司', 4, '国药准字H32024826', 1, '86901453000855', 2, 1, '化学药品'),
(22, '注射用头孢他啶', '注射剂', '60.00', 198, '0.5g', '三才石岐制药股份有限公司', 3, '国药准字H20055694', 3, '86900322001887', 1, 1, '化学药品'),
(23, '注射用促肝细胞生长素', '注射剂', '350.00', 120, '20mg', '吉林敖东药业集团延吉股份有限公司', 4, '国药准字H22025538', 1, '86903358000695', 1, 2, '化学药品'),
(24, '利巴韦林注射液', '注射剂', '27.00', 350, '1ml:0.1g', '浙江诚意药业股份有限公司', 3, '国药准字H19993829', 4, '86904615000533', 1, 1, '化学药品'),
(25, '黄体酮注射液', '注射剂', '44.00', 360, '1ml:20mg', '天津金耀药业有限公司', 4, '国药准字H12020533', 2, '86900874000475', 2, 1, '化学药品'),
(26, '阿苯达唑片', '片剂', '18.80', 240, '0.1g', '安徽圣鹰药业有限公司', 4, '国药准字H34023411', 5, '86904344000026', 1, 1, '化学药品'),
(27, '吡喹酮片', '片剂', '50.00', 310, '0.2g', '上海信谊天平药业有限公司', 1, '国药准字H31020485', 5, '86900681000125', 2, 2, '化学药品'),
(28, '海正麦克丁', '片剂', '26.00', 180, '3mg', '浙江海正药业股份有限公司', 2, '国药准字H20041990', 5, '86904641001351', 1, 1, '化学药品'),
(29, '氨硫脲片', '片剂', '155.00', 166, '25mg', '北京京丰制药（山东）有限公司', 3, '国药准字H37020444', 5, '86904105000050', 2, 1, '化学药品'),
(30, '磷酸氯喹片', '片剂', '130.00', 201, '0.25g', '三才石岐制药股份有限公司', 1, '国药准字H44023257', 5, '86900322001504', 2, 1, '化学药品'),
(31, '复方三嗪芦丁片', '片剂', '33.00', 210, '0.15g', '赤峰维康生化制药有限公司', 4, '国药准字H15021431', 5, '86903870000630', 2, 1, '化学药品'),
(32, '复方奎宁注射液', '注射剂', '25.00', 321, '2ml', '国药集团国瑞药业有限公司', 2, '国药准字H34023656', 5, '86900372010878', 2, 2, '化学药品'),
(33, '盐酸左旋咪唑片', '片剂', '3.00', 565, '25mg', '广州白云山光华制药股份有限公司', 4, '国药准字H44020143', 5, '86900372000878', 1, 1, '化学药品'),
(34, '氯硝柳胺', '原料药', '60.00', 166, '0.1g', '恒诚制药集团淮南有限公司', 2, '国药准字H34022426', 6, '86904285000581', 1, 2, '化学药品'),
(35, '盐酸多巴胺', '原料药', '190.00', 123, '0.2g', '常州亚邦制药有限公司', 3, '国药准字H20053177', 5, '86901394000358', 2, 2, '化学药品'),
(36, '乙酰螺旋霉素片', '片剂', '12.00', 369, '0.2g', '甘肃兰药药业有限公司', 4, '国药准字H62020697', 7, '86905863002249', 1, 1, '化学药品'),
(37, '甲硝唑', '片剂', '29.00', 290, '0.2g', '上海金不换兰考制药有限公司', 1, '国药准字H41021614', 7, '86903059000611', 1, 2, '化学药品'),
(38, '甲硝唑氯化钠注射液', '注射剂', '66.00', 266, '250ml', '吉林省都邦药业股份有限公司', 4, '国药准字H22023068', 7, '86903459000426', 2, 1, '化学药品'),
(39, '青霉素钠', '注射剂', '39.90', 299, '0.48g', '山西振东泰盛制药有限公司', 2, '国药准字H14020377', 7, '86902946000611', 2, 1, '化学药品'),
(40, '环孢素软胶囊', '胶囊剂', '165.00', 165, '50mg', '华北制药股份有限公司', 3, '国药准字H10960008', 7, '86902697000243', 1, 1, '化学药品'),
(41, '硫酸阿托品片', '片剂', '15.80', 158, '0.3mg', '江苏天士力帝益药业有限公司', 2, '国药准字H32020319', 7, '86901500000838', 2, 2, '化学药品'),
(42, '咪达唑仑注射液', '注射剂', '33.00', 133, '2ml:10mg', '宜昌人福药业有限责任公司', 4, '国药准字H20067041', 7, '86902000001073', 1, 1, '化学药品'),
(43, '硫酸卡那霉素胶囊', '胶囊剂', '96.00', 100, '0.125g', '长春迪瑞制药有限公司', 2, '国药准字H22024454', 6, '86903305001256', 1, 1, '化学药品'),
(44, '妥布霉素吸入溶液', '吸入制剂', '6799.00', 50, '5ml:300mg', '健康元海滨药业有限公司', 2, '国药准字H20220025', 6, '86900545000131', 1, 2, '化学药品'),
(45, '阿米卡星', '原料药', '22.00', 222, '0.15g', '浙江金华康恩贝生物制药有限公司', 2, '国药准字H33021380', 6, '86904656000028', 1, 1, '化学药品'),
(46, '烟酸占替诺片', '片剂', '16.00', 100, '100mg', '内蒙古海天制药有限公司', 2, '国药准字H15021249', 6, '86903899000956', 1, 2, '化学药品'),
(47, '异烟肼片', '片剂', '26.00', 256, '50mg', '国药集团国瑞药业有限公司', 2, '国药准字H34023146', 6, '86904383001336', 2, 2, '化学药品'),
(48, '盐酸乙胺丁醇胶囊', '胶囊剂', '28.00', 280, '0.25g', '山西好医生药业有限公司', 4, '国药准字H14023133', 6, '86902849000602', 1, 1, '化学药品'),
(49, '吡嗪酰胺片', '片剂', '38.00', 138, '0.5g', '杭州民生药业股份有限公司', 4, '国药准字H51022127', 6, '86902020000056', 1, 1, '化学药品'),
(50, '马来酸伊索拉定片', '片剂', '65.00', 165, '2mg', '齐鲁制药有限公司', 2, '国药准字H10980048', 6, '86904021000899', 2, 2, '化学药品'),
(51, '抗病毒颗粒', '颗粒', '35.00', 345, '4g', '四川光大制药有限公司', 3, '国药准字Z20010127', 4, '86902144000383', 2, 1, '中药'),
(52, '抗病毒口服液', '合剂', '27.00', 217, '10ml', '江西青峰药业有限公司', 4, '国药准字Z20044129', 4, '86905337000269', 1, 2, '中药'),
(53, '射干抗病毒注射液', '注射剂', '59.00', 159, '2ml', '朗致集团万荣药业有限公司', 2, '国药准字Z14020996', 4, '86902982001320', 1, 1, '中药'),
(54, '四季抗病毒胶囊', '胶囊剂', '81.00', 381, '0.38g', '陕西海天制药有限公司', 4, '国药准字Z20050328', 4, '86902371000149', 2, 1, '中药'),
(55, '磷酸奥司他韦胶囊', '胶囊剂', '79.00', 279, '75mg', '北京双鹭药业股份有限公司', 1, '国药准字H20223919', 4, '86900148001436', 2, 2, '化学药品'),
(56, '戈诺卫', '片剂', '159.00', 259, '100mg', '歌礼药业（浙江）有限公司', 3, '国药准字H20180008', 4, '86981008000011', 2, 1, '化学药品'),
(57, '人干扰素α2b栓', '栓剂', '132.00', 132, '50万IU/枚', '长春生物制品研究所有限责任公司', 3, '国药准字S20100006', 4, '86903320001491', 2, 1, '生物制品'),
(58, '阿昔洛韦', '片剂', '15.00', 155, '0.1g', '云南植物药业有限公司', 3, '国药准字H53020386', 4, '86905613000051', 2, 2, '化学药品'),
(59, '胃蛋白酶片', '片剂', '21.00', 221, '120单位', '漯河汇盛药业有限公司', 4, '国药准字H19993521', 1, '86903116000165', 1, 1, '化学药品'),
(60, '拉米夫定片', '片剂', '133.00', 233, '0.15g', '中孚药业股份有限公司', 2, '国药准字H20133057', 4, '86904180001300', 1, 1, '化学药品'),
(61, '阿司匹林散', '散剂', '68.00', 168, '0.5g', '浙江巨泰药业有限公司', 2, '国药准字H10950261', 2, '86904667000055', 1, 2, '化学药品'),
(62, '奥美拉唑肠溶胶囊', '胶囊剂', '58.00', 258, '20mg', '海南普利制药股份有限公司', 4, '国药准字H20113282', 2, '86905801000672', 1, 1, '化学药品'),
(63, '雷贝拉唑钠肠溶胶囊', '胶囊剂', '40.00', 240, '20mg', '济川药业集团有限公司', 2, '国药准字H20061220', 2, '86901453001548', 1, 2, '化学药品'),
(64, '苯磺酸氨氯地平片', '片剂', '60.00', 260, '5mg', '乐普药业（北京）有限责任公司', 2, '国药准字H20074084', 1, '86900205000365', 2, 1, '化学药品'),
(65, '注射用奥沙利铂', '注射剂', '1290.00', 30, '50mg', '哈药集团生物工程有限公司', 2, '国药准字H20133094', 2, '86903708000511', 1, 1, '化学药品'),
(66, '培唑帕尼片', '片剂', '1690.00', 40, '0.2g', '齐鲁制药有限公司', 2, '国药准字H20233248', 2, '86904021004675', 1, 1, '化学药品'),
(67, '重酒石酸卡巴拉汀胶囊', '胶囊剂', '315.00', 100, '3.0mg', '北京四环制药有限公司', 4, '国药准字H20203012', 2, '86900153000790', 1, 1, '化学药品'),
(68, '注射用曲妥珠单抗', '注射剂', '4498.00', 25, '150mg/瓶', '上海复宏汉霖生物制药有限公司', 2, '国药准字S20200019', 1, '86982144000033', 1, 1, '生物制品'),
(69, '甲磺酸阿帕替尼片', '片剂', '430.00', 98, '0.375g', '江苏恒瑞医药股份有限公司', 2, '国药准字H20140104', 4, '86901445002805', 1, 1, '化学药品'),
(70, '依托红霉素片', '片剂', '26.00', 326, '0.125g', '惠州大亚制药股份有限公司', 3, '国药准字H44020836', 4, '86900434000099', 1, 1, '化学药品'),
(71, '氟康唑胶囊', '胶囊剂', '32.00', 325, '50mg', '湖北恒安芙林药业股份有限公司', 3, '国药准字H20093948', 3, '86901808000233', 2, 2, '化学药品'),
(72, '复方酮康唑乳膏', '乳膏剂', '27.00', 427, '10g', '江苏晨牌邦德药业有限公司', 4, '国药准字H20057782', 3, '86901664000040', 2, 1, '化学药品'),
(73, '伊曲康唑胶囊', '胶囊剂', '19.50', 295, '0.1g', '乐普药业股份有限公司', 1, '国药准字H20090329', 3, '86903094000768', 1, 1, '化学药品'),
(74, '盐酸阿莫罗芬搽剂', '搽剂', '218.00', 200, '5%', '江苏福邦药业有限公司', 3, '国药准字H20123162', 3, '86901438000252', 2, 1, '化学药品'),
(75, '注射用醋酸卡泊芬净', '注射剂', '240.00', 124, '70mg', '杭州中美华东制药有限公司', 2, '国药准字H20237029', 3, '86904520000956', 1, 1, '化学药品'),
(76, '伏立康唑片', '片剂', '758.00', 58, '50mg', '晋城海斯制药有限公司', 2, '国药准字H20213893', 3, '86902856001395', 1, 1, '化学药品'),
(77, '氟康唑胶囊', '胶囊剂', '32.00', 232, '50mg', '湖北恒安芙林药业股份有限公司', 1, '国药准字H20093948', 3, '86901808000233', 2, 1, '化学药品'),
(78, '盐酸阿莫罗芬搽剂', '搽剂', '108.00', 108, '2.5ml:0.125g', '浙江迪耳药业有限公司', 1, '国药准字H20065886', 2, '86904623000686', 2, 1, '化学药品'),
(79, '氯霉素片', '片剂', '24.00', 240, '0.25g', '锦州奥鸿药业有限责任公司', 1, '国药准字H21021877', 2, '86901190000101', 2, 1, '化学药品'),
(80, '硫酸庆大霉素缓释片', '缓释制剂', '15.00', 345, '40mg', '上海迪冉郸城制药有限公司', 1, '国药准字H20013270', 2, '86903034000179', 2, 1, '化学药品'),
(81, '妥布霉素滴眼液', '眼用制剂', '18.00', 288, '5ml:15mg', '成都倍特药业股份有限公司', 1, '国药准字H20046527', 2, '86902138000214', 2, 1, '化学药品'),
(82, '罗红霉素颗粒', '颗粒', '5.00', 500, '50mg', '深圳海王药业有限公司', 1, '国药准字H20073899', 2, '86900503000753', 2, 1, '化学药品'),
(83, '克拉霉素缓释胶囊', '缓释胶囊剂', '25.50', 255, '0.25g', '广州柏赛罗药业有限公司', 1, '国药准字H20051661', 2, '86900387000146', 2, 1, '化学药品'),
(84, '一次性使用医用口罩', '医疗器械', '9.90', 599, '175mm×95mm', '广东省格美尔医疗科技有限公司', 1, '粤械注准20202141205', 1, '无', 2, 1, '医疗器械'),
(85, '苯磺酸氨氯地平滴丸', '滴丸剂', '168.00', 168, '5mg', '北京九龙制药有限公司', 2, '国药准字H20080728', 1, '86900067000244', 2, 1, '化学药品'),
(86, '格列美脲胶囊', '胶囊剂', '70.00', 170, '2mg', '广西百琪药业有限公司', 3, '国药准字H20030283', 1, '86905071000211', 2, 1, '化学药品'),
(87, '环孢素软胶囊', '胶囊剂', '220.00', 122, '50mg', '华北制药股份有限公司', 4, '国药准字H10960008', 2, '86902697000243', 2, 1, '化学药品'),
(88, '华法林钠片', '片剂', '55.00', 255, '5mg', '北京嘉林药业股份有限公司', 4, '国药准字H20054247', 1, '86900056000217', 2, 1, '化学药品'),
(89, '甲氨蝶呤片', '片剂', '156.00', 156, '2.5mg', '上海上药信谊药厂有限公司', 2, '国药准字H31020644', 1, '86900818002275', 2, 1, '化学药品'),
(90, '补肺丸', '丸剂', '960.00', 96, '1.5g', '丽彩甘肃西峰制药有限公司', 1, '国药准字Z62020558', 1, '86909579000063', 2, 1, '中药'),
(91, '虫草清肺胶囊', '胶囊剂', '225.00', 125, '0.3g', '青海普兰特药业有限公司', 1, '国药准字Z20025121', 1, '86905939000018', 2, 1, '中药'),
(92, '米诺地尔凝胶', '凝胶剂', '148.00', 148, '40g:0.88g', '山东博士伦福瑞达制药有限公司', 3, '国药准字H20050314', 1, '86904072000688', 2, 1, '化学药品'),
(93, '甲硝唑凝胶', '凝胶剂', '29.00', 229, '0.75%', '海南海神同洲制药有限公司', 1, '国药准字H20113203', 2, '86905777000607', 2, 1, '化学药品'),
(94, '阿达帕林凝胶', '凝胶剂', '29.90', 129, '0.1%', '黑龙江福和制药集团股份有限公司', 1, '国药准字H20056871', 2, '86903731000014', 2, 1, '化学药品'),
(95, '连花清瘟胶囊', '胶囊剂', '14.50', 445, '0.35g', '衡水以岭药业有限公司', 1, '国药准字Z20040063', 4, '86902767000395', 2, 1, '中药'),
(96, '复方金银花颗粒', '颗粒', '28.00', 328, '0.35g', '哈尔滨仁皇药业有限公司', 1, '国药准字Z23020508', 4, '86903658000074', 2, 1, '中药'),
(97, '板蓝根颗粒', '颗粒', '18.80', 488, '3g', '国药集团德众(佛山)药业有限公司', 1, '国药准字Z44021345', 4, '86900255000018', 2, 1, '中药'),
(98, '铝碳酸镁咀嚼片', '片剂', '34.00', 340, '0.5g', '安丘市鲁安药业有限责任公司', 1, '国药准字H10950011', 1, '86903937000399', 2, 1, '化学药品'),
(99, '硫糖铝混悬凝胶', '凝胶剂', '33.00', 233, '5ml:1g', '昆明积大制药股份有限公司', 1, '国药准字H20080322', 1, '86905589000864', 2, 1, '化学药品'),
(100, '布洛芬胶囊', '胶囊剂', '29.80', 398, '0.2g', '山西宝泰药业有限责任公司', 2, '国药准字H14023609', 1, '86902871000205', 2, 1, '化学药品'),
(101, '氨咖黄敏胶囊', '胶囊剂', '16.90', 269, '0.1g', '吉林华康药业股份有限公司', 1, '国药准字H22024309', 1, '86903373000052', 2, 1, '中药'),
(102, '云南白药气雾剂', '气雾剂', '59.80', 298, '85g', '云南白药集团股份有限公司', 1, '国药准字Z53021105', 1, '86905629000854', 2, 1, '中药'),
(103, '健胃消食片', '片剂', '13.30', 333, '0.8g', '甘肃普安制药股份有限公司', 1, '国药准字Z20083398', 1, '86905869000065', 2, 1, '中药'),
(104, '速效救心丸', '滴丸剂', '33.50', 315, '40mg', '津药达仁堂集团股份有限公司第六中药厂', 1, '国药准字Z12020025', 1, '86900961000067', 1, 1, '中药'),
(105, '复方丹参片', '片剂', '23.00', 323, '0.3g', '特一药业集团股份有限公司', 1, '国药准字Z20083442', 1, '86900281001034', 2, 1, '中药'),
(106, '藿香正气水', '酊剂', '5.00', 342, '10ml', '药都制药集团股份有限公司', 1, '国药准字Z34020929', 1, '86904366000547', 2, 1, '中药'),
(107, '肠炎宁胶囊', '胶囊剂', '19.50', 295, '0.42g', '江西康恩贝天施康药业有限公司', 1, '国药准字Z20050191', 1, '86905363002473', 2, 1, '中药'),
(108, '复方黄连素片', '片剂', '12.80', 360, '30mg', '四川古蔺肝苏药业有限公司', 1, '国药准字Z51021839', 4, '86902183000160', 2, 1, '中药'),
(109, '正红花油', '搽剂', '16.00', 256, '20ml', '成都东洋百信制药有限公司', 1, '国药准字Z20033087', 1, '86902021000109', 2, 1, '中药'),
(110, '小儿清咽冲剂', '颗粒', '28.80', 288, '6g', '宁夏启元国药有限公司', 1, '国药准字Z64020073', 1, '86905914002235', 2, 1, '中药'),
(111, '盐酸金霉素眼膏', '眼膏剂', '6.50', 365, '0.5%', '山东辰欣佛都药业股份有限公司', 1, '国药准字H37021990', 2, '86904127002155', 2, 1, '化学药品'),
(112, '牛黄解毒片', '片剂', '24.50', 245, '30mg', '四川依科制药有限公司', 1, '国药准字Z20020113', 1, '86902251000733', 2, 1, '中药'),
(113, '静注人免疫球蛋白(pH4)', '注射剂', '744.00', 80, '2.5g/50ml/瓶', '武汉中原瑞德生物制品有限责任公司', 3, '国药准字S20013003', 1, '86901959000014', 1, 1, '药品'),
(114, '复方氨酚烷胺片', '片剂', '28.00', 350, '0.1g', '长沙东风药业有限公司', 1, '国药准字H43021999', 1, '86904886000393', 2, 1, '化学药品'),
(115, '感冒灵123', 's', '0.00', 2, '0.1g', '2222', 2, '国药', 1, '2222', 1, 1, '中'),
(116, 'aaaa', 'asd', '0.00', 2, '0.1g', 'XXX', 1, '国药准字H43021999', 1, '86904886000393', 2, 2, '器械');

-- --------------------------------------------------------

--
-- 表的结构 `app_ruku`
--

DROP TABLE IF EXISTS `app_ruku`;
CREATE TABLE IF NOT EXISTS `app_ruku` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `drug_name` varchar(32) NOT NULL,
  `in_money` decimal(10,2) NOT NULL,
  `in_number` int DEFAULT NULL,
  `in_time` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=115 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_ruku`
--

INSERT INTO `app_ruku` (`id`, `drug_name`, `in_money`, `in_number`, `in_time`) VALUES
(1, '速效救心丸', '900.00', 30, '2023-01-01'),
(2, '速效救心丸', '900.00', 30, '2023-01-01'),
(3, '速效救心丸', '1200.00', 40, '2023-02-01'),
(4, '速效救心丸', '1500.00', 50, '2023-03-01'),
(5, '速效救心丸', '1800.00', 60, '2023-04-01'),
(6, '速效救心丸', '1500.00', 50, '2023-05-01'),
(7, '速效救心丸', '900.00', 30, '2023-06-01'),
(8, '速效救心丸', '900.00', 30, '2023-07-01'),
(9, '速效救心丸', '900.00', 30, '2023-08-01'),
(10, '速效救心丸', '1500.00', 50, '2023-09-01'),
(11, '速效救心丸', '1500.00', 50, '2023-10-01'),
(12, '速效救心丸', '3000.00', 100, '2023-11-01'),
(13, '速效救心丸', '900.00', 30, '2023-12-01'),
(14, '速效救心丸', '1200.00', 40, '2024-01-01'),
(15, '速效救心丸', '1200.00', 40, '2024-02-01'),
(16, '速效救心丸', '1200.00', 40, '2024-03-01'),
(17, '速效救心丸', '900.00', 30, '2024-04-01'),
(18, '速效救心丸', '900.00', 30, '2024-05-01'),
(19, '速效救心丸', '1500.00', 50, '2024-06-01'),
(20, '速效救心丸', '1500.00', 50, '2024-07-01'),
(21, '速效救心丸', '1800.00', 60, '2024-08-01'),
(22, '速效救心丸', '1800.00', 60, '2024-09-01'),
(23, '速效救心丸', '2100.00', 70, '2024-10-01'),
(24, '速效救心丸', '120.00', 40, '2024-11-01'),
(25, '速效救心丸', '300.00', 10, '2024-12-01'),
(26, '速效救心丸', '900.00', 30, '2025-01-01'),
(27, '速效救心丸', '600.00', 20, '2025-02-01'),
(28, '速效救心丸', '900.00', 30, '2025-03-01'),
(29, '速效救心丸', '900.00', 30, '2025-04-01'),
(30, '速效救心丸', '2400.00', 80, '2025-05-01'),
(31, '速效救心丸', '1800.00', 60, '2025-06-01'),
(32, '速效救心丸', '600.00', 20, '2025-07-01'),
(33, '速效救心丸', '900.00', 30, '2025-08-01'),
(34, '速效救心丸', '2100.00', 70, '2025-09-01'),
(35, '速效救心丸', '2100.00', 70, '2025-10-01'),
(36, '速效救心丸', '900.00', 30, '2025-11-01'),
(37, '速效救心丸', '1500.00', 50, '2025-12-01'),
(38, '藿香正气水', '400.00', 80, '2023-01-12'),
(39, '藿香正气水', '50.00', 10, '2023-01-12'),
(40, '藿香正气水', '400.00', 80, '2023-02-12'),
(41, '藿香正气水', '200.00', 40, '2023-03-12'),
(42, '藿香正气水', '200.00', 40, '2023-04-12'),
(43, '藿香正气水', '400.00', 80, '2023-05-12'),
(44, '藿香正气水', '450.00', 90, '2023-06-12'),
(45, '藿香正气水', '500.00', 100, '2023-07-12'),
(46, '藿香正气水', '500.00', 100, '2023-08-12'),
(47, '藿香正气水', '150.00', 30, '2023-09-12'),
(48, '藿香正气水', '200.00', 40, '2023-10-12'),
(49, '藿香正气水', '300.00', 60, '2023-11-12'),
(50, '藿香正气水', '350.00', 70, '2023-12-12'),
(51, '藿香正气水', '300.00', 60, '2024-01-12'),
(52, '藿香正气水', '400.00', 80, '2024-02-12'),
(53, '藿香正气水', '200.00', 40, '2024-03-12'),
(54, '藿香正气水', '200.00', 40, '2024-04-12'),
(55, '藿香正气水', '400.00', 80, '2024-05-12'),
(56, '藿香正气水', '450.00', 90, '2024-06-12'),
(57, '藿香正气水', '500.00', 100, '2024-07-12'),
(58, '藿香正气水', '500.00', 100, '2024-08-12'),
(59, '藿香正气水', '150.00', 30, '2024-09-12'),
(60, '藿香正气水', '200.00', 40, '2024-10-12'),
(61, '藿香正气水', '300.00', 60, '2024-11-12'),
(62, '藿香正气水', '350.00', 70, '2024-12-12'),
(63, '藿香正气水', '500.00', 100, '2025-01-12'),
(64, '藿香正气水', '400.00', 80, '2025-02-12'),
(65, '藿香正气水', '200.00', 40, '2025-03-12'),
(66, '藿香正气水', '200.00', 40, '2025-04-12'),
(67, '藿香正气水', '400.00', 80, '2025-05-12'),
(68, '藿香正气水', '450.00', 90, '2025-06-12'),
(69, '藿香正气水', '500.00', 100, '2025-07-12'),
(70, '藿香正气水', '500.00', 100, '2025-08-12'),
(71, '藿香正气水', '150.00', 30, '2025-09-12'),
(72, '藿香正气水', '200.00', 40, '2025-10-12'),
(73, '藿香正气水', '300.00', 60, '2025-11-12'),
(74, '藿香正气水', '350.00', 70, '2025-12-12'),
(75, '抗病毒颗粒', '900.00', 30, '2023-01-01'),
(76, '抗病毒颗粒', '900.00', 30, '2023-01-01'),
(77, '抗病毒颗粒', '1200.00', 40, '2023-02-01'),
(78, '抗病毒颗粒', '1800.00', 60, '2023-03-01'),
(79, '抗病毒颗粒', '900.00', 30, '2023-04-01'),
(80, '抗病毒颗粒', '1200.00', 40, '2023-05-01'),
(81, '抗病毒颗粒', '1500.00', 50, '2023-06-01'),
(82, '抗病毒颗粒', '1500.00', 50, '2023-07-01'),
(83, '抗病毒颗粒', '2100.00', 70, '2023-08-01'),
(84, '抗病毒颗粒', '900.00', 30, '2023-09-01'),
(85, '抗病毒颗粒', '1200.00', 40, '2023-10-01'),
(86, '抗病毒颗粒', '2400.00', 80, '2023-11-01'),
(87, '抗病毒颗粒', '2100.00', 70, '2023-12-01'),
(88, '阿司匹林散', '1800.00', 30, '2023-01-28'),
(89, '阿司匹林散', '1800.00', 30, '2023-01-28'),
(90, '阿司匹林散', '1800.00', 30, '2023-02-28'),
(91, '阿司匹林散', '3600.00', 60, '2023-03-28'),
(92, '阿司匹林散', '3000.00', 50, '2023-04-28'),
(93, '阿司匹林散', '3000.00', 50, '2023-05-28'),
(94, '阿司匹林散', '2400.00', 40, '2023-06-28'),
(95, '阿司匹林散', '3600.00', 60, '2023-07-28'),
(96, '阿司匹林散', '3300.00', 55, '2023-08-28'),
(97, '阿司匹林散', '2700.00', 45, '2023-09-28'),
(98, '阿司匹林散', '2400.00', 40, '2023-10-28'),
(99, '阿司匹林散', '2100.00', 35, '2023-11-28'),
(100, '阿司匹林散', '4200.00', 70, '2023-12-28'),
(101, '复方酮康唑乳膏', '1200.00', 40, '2023-01-17'),
(102, '复方酮康唑乳膏', '900.00', 30, '2023-02-07'),
(103, '复方酮康唑乳膏', '1800.00', 60, '2023-03-03'),
(104, '复方酮康唑乳膏', '1500.00', 50, '2023-04-08'),
(105, '复方酮康唑乳膏', '2100.00', 70, '2023-05-05'),
(106, '复方酮康唑乳膏', '1500.00', 50, '2023-06-17'),
(107, '复方酮康唑乳膏', '1800.00', 60, '2023-07-17'),
(108, '复方酮康唑乳膏', '1200.00', 40, '2023-08-17'),
(109, '复方酮康唑乳膏', '1500.00', 50, '2023-09-17'),
(110, '复方酮康唑乳膏', '1500.00', 50, '2023-10-17'),
(111, '复方酮康唑乳膏', '1800.00', 60, '2023-11-17'),
(112, '复方酮康唑乳膏', '2100.00', 70, '2023-12-17'),
(113, '藿香正气水', '10.00', 1, '2023-05-01'),
(114, '藿香正气水', '5.00', 1, '2025-05-25');

-- --------------------------------------------------------

--
-- 表的结构 `app_user`
--

DROP TABLE IF EXISTS `app_user`;
CREATE TABLE IF NOT EXISTS `app_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_user`
--

INSERT INTO `app_user` (`id`, `username`, `password`) VALUES
(1, 'user', 'pbkdf2_sha256$600000$H6GkrgpgW0gsRtsgP9uBcK$mFK/85xajlomwislgSwAGaL3B8p3Pc4GkCxSv+xTLFo='),
(2, '1137244573', 'pbkdf2_sha256$600000$RprujjWqsuLlIzdk6LyJC6$0VivNiLAb2flSS6prgIugBFvrWebrVZ2OGwwQeJuNQk='),
(3, 'user1', 'pbkdf2_sha256$600000$p4IctOHkJhAGE3PnWMiwSS$lWvzvGQZp6BZ6NhbU2NDGDmXvGf9frrG8+kbY/Mbl94='),
(4, 'user2', 'pbkdf2_sha256$600000$lwoHPMJGumLvK64MPW6X3A$7QBOx44kNwExhyNZXhX12l8yHMqO7yEx820ureO4oc4='),
(5, 'user3', 'pbkdf2_sha256$600000$cpppoAiiHdQzOQYWILDHa1$ovxKu+oC7Sjmzv23zEPxZ0vB09mUDMivYMdfouTVhJM='),
(6, '123', 'pbkdf2_sha256$600000$GmI6wHOciWTqLd9nBz4dNL$XVPgrdxpiEt5KG/JR3IcpAkan3O5pHXVMw7hVrWpGAg=');

-- --------------------------------------------------------

--
-- 表的结构 `app_work`
--

DROP TABLE IF EXISTS `app_work`;
CREATE TABLE IF NOT EXISTS `app_work` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `time` date NOT NULL,
  `name` varchar(64) NOT NULL,
  `phone` varchar(64) NOT NULL,
  `gender` smallint NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `app_work`
--

INSERT INTO `app_work` (`id`, `username`, `password`, `time`, `name`, `phone`, `gender`) VALUES
(1, '20000101', 'pbkdf2_sha256$600000$pbGWNI3XFnho5CtnPTY0cj$/krKqsJVZGIa02sfjHlTB5grEw30rLGfgkLnxQW1jCY=', '2023-01-01', '杞宏旷', '13227822781', 2),
(2, '20230202', 'pbkdf2_sha256$600000$kToEYlXdOGzlVUHGtq0SCi$i48L9BN/1d38Dk6sR89MAX0ple1srRnGla7QpCnoAaI=', '2023-02-01', '隆雪羽', '15191805293', 2),
(3, '20230303', 'pbkdf2_sha256$600000$wEv60hGtTyNG8TjaJdP7AC$HcYP8v5nLdU6FsUVb4mH+QePgK6kUUZdYQ4T6kdmxEc=', '2023-03-01', '却若云', '18829708956', 1),
(4, '20230404', 'pbkdf2_sha256$600000$YNFdoxkpfv21tLsEXban7Z$Pif0Zgqnl+dk0xsjj50hUJJC0PjwXAnM6GBlTEayHJs=', '2023-04-12', '桓鸣', '15939737978', 1),
(5, '20230505', 'pbkdf2_sha256$600000$0ESvut7YjA4xW6jGjRUlhB$ejK7BYWQRgr02bBhRPk0lnla5hSmP6vbLGbiPMJAlw0=', '2023-05-12', '寇敬曦', '17293504672', 2),
(6, '20230606', 'pbkdf2_sha256$600000$orCZ2FWQnKsqKRJggUxKxk$kQzrG11GYyoMH+6nHGAf+6BFZ7cm4AJBULtQMe+xbqM=', '2023-06-14', '季听双', '14944226503', 2),
(7, '20230707', 'pbkdf2_sha256$600000$ystJSaTQ8dFmTst3gqzqpG$tMHAlrsC1W9zAX26QRFIGlO2iXe3TtKlxGYRfBNwW4c=', '2023-07-13', '望鸿云', '18731931153', 1),
(8, '20230808', 'pbkdf2_sha256$600000$TpDlKv5nREnad7XJbJIqmt$7gSe1MppraBgdq6lqW1wDsIzxKaC6hRo3Jkj/VPUmp0=', '2023-08-16', '泣冰凡', '17372246941', 2),
(9, '20230909', 'pbkdf2_sha256$600000$MX2Z0Rwq1KDKgndTB7PBfN$yRQRD50M21emCAJV1leP/vBOdarW8O1tXY3N9ZzEKiE=', '2023-09-07', '宦采文', '18348219848', 1),
(10, '20231010', 'pbkdf2_sha256$600000$wHzlsk6FprMHJyduMa7Akg$Hs000KL+4tpyI0RS+u/1WxjyoXzx7QMaiDLcr99awdI=', '2023-10-27', '娄凌柏', '15642328789', 2),
(13, '20010606', 'pbkdf2_sha256$600000$ckrYvYbKngaXYGdlPqedlg$09SrZdUQH6XZqAnU9aIHqkgXk8+udRFg4xY4re6nWCs=', '2023-06-19', '李润晨', '18829708555', 1);

-- --------------------------------------------------------

--
-- 表的结构 `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- 表的结构 `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-05-28 13:32:08.957992'),
(2, 'auth', '0001_initial', '2023-05-28 13:32:09.477219'),
(3, 'admin', '0001_initial', '2023-05-28 13:32:09.599290'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-05-28 13:32:09.606335'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-05-28 13:32:09.614323');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `session_data` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('fkdrcjyu9cf65bbuct9tuh74bnmuceov', 'e30:1pypyt:RUUDzvjAHqBV8nJOHNNQo_Rs72MJEn2CJjoJfoQPyu8', '2023-05-30 08:24:27.089949'),
('r9kiokgwhddoquwtv76i2d56trvpy5s7', 'eyJpbmZvIjp7ImlkIjoxLCJuYW1lIjoiYWRtaW4ifX0:1q3z3o:mKBbKItjq5DIlqck4M3JtyudK8kru6bAh_-mW6HIckg', '2023-06-13 13:06:48.361939'),
('2ipcmqeowp88z81qy2ydhsx3jpwhiiuu', 'eyJpbmZvIjp7ImlkIjoxLCJuYW1lIjoiYWRtaW4ifX0:1qAPpg:3dJ3HtjSdLIE99L705eBuhIh7b8qaj8UyGGOpSIdfcU', '2023-07-01 06:54:48.874708');

--
-- 限制导出的表
--

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
