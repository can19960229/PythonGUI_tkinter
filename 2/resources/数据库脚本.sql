1、
-- 【注释】判断user表是否存在，如果存在则进行删除
DROP TABLE IF EXISTS user ;
-- 【注释】创建user表，同时为每一个列设置说明信息
CREATE TABLE user(
	uid BIGINT AUTO_INCREMENT COMMENT '主键列（自动增长）',
	name VARCHAR(30) COMMENT '用户姓名' ,
	age INT COMMENT '用户年龄' ,
	birthday DATE COMMENT '用户生日' ,
	salary FLOAT COMMENT '用户月薪' ,
	note TEXT COMMENT '用户说明' ,
	CONSTRAINT pk_uid PRIMARY KEY(uid)
) engine=INNODB ;


2、
-- 【注释】删除数据库
DROP DATABASE IF EXISTS mypythondemo
-- 【注释】创建数据库
CREATE DATABASE mypythondemo CHARACTER SET UTF8
-- 【注释】使用数据库
use mypythondemo
-- 【注释】判断user表是否存在，如果存在则进行删除
DROP TABLE IF EXISTS test;
-- 【注释】创建user表，同时为每一个列设置说明信息
CREATE TABLE test(
	uid BIGINT AUTO_INCREMENT COMMENT '主键列（自动增长）',
	name VARCHAR(30) COMMENT '用户姓名' ,
	age INT COMMENT '用户年龄' ,
	birthday DATE COMMENT '用户生日' ,
	salary FLOAT COMMENT '用户月薪' ,
	note TEXT COMMENT '用户说明' ,
	CONSTRAINT pk_uid PRIMARY KEY(uid)
) engine=INNODB ;
INSERT INTO test(name,age,birthday,salary,note) VALUES ('陈灿',20,'2008-08-13',8000.00,'www.baidu.com');
INSERT INTO test(name,age,birthday,salary,note) VALUES ('陈蒸鱼',10,'2007-08-13',9000.00,'www.baidu.com');
INSERT INTO test(name,age,birthday,salary,note) VALUES ('陈七七',28,'2006-08-13',6000.00,'www.baidu.com');



3、
-- 【注释】判断数据表是否存在，如果存在则进行删除
DROP TABLE IF EXISTS dept ;
DROP TABLE IF EXISTS company ;
-- 【注释】创建数据表表，同时为每一个列设置说明信息
CREATE TABLE company(
	cid		VARCHAR(20) 		COMMENT '主键列（以字母C开头）',
	cname	VARCHAR(50) 		COMMENT '公司名称' ,
	site		VARCHAR(200)		COMMENT '公司网址' ,
	CONSTRAINT pk_cid PRIMARY KEY(cid)
) engine=INNODB ;
CREATE TABLE dept(
	did		BIGINT		AUTO_INCREMENT 	COMMENT '主键列（自动增长）',
	dname	VARCHAR(50) 						COMMENT '部门名称' ,
	cid		VARCHAR(20)						COMMENT '公司编号，对应company.cid' ,
	CONSTRAINT pk_did PRIMARY KEY(did),
	CONSTRAINT fk_cid FOREIGN KEY(cid) REFERENCES company(cid) ON DELETE CASCADE
) engine=INNODB ;
-- 【注释】向表中追加测试数据
INSERT INTO company(cid,cname,site) VALUES ('C-001', '沐言童趣科技公司', 'www.kidhalo.com') ;
INSERT INTO dept(dname,cid) VALUES ('教学管理部', 'C-001') ;
INSERT INTO dept(dname,cid) VALUES ('教材研发部', 'C-001') ;
INSERT INTO dept(dname,cid) VALUES ('软件工程部', 'C-001') ;
-- 【注释】提交事务
COMMIT ;
