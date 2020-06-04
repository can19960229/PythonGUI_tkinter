1��
-- ��ע�͡��ж�user���Ƿ���ڣ�������������ɾ��
DROP TABLE IF EXISTS user ;
-- ��ע�͡�����user��ͬʱΪÿһ��������˵����Ϣ
CREATE TABLE user(
	uid BIGINT AUTO_INCREMENT COMMENT '�����У��Զ�������',
	name VARCHAR(30) COMMENT '�û�����' ,
	age INT COMMENT '�û�����' ,
	birthday DATE COMMENT '�û�����' ,
	salary FLOAT COMMENT '�û���н' ,
	note TEXT COMMENT '�û�˵��' ,
	CONSTRAINT pk_uid PRIMARY KEY(uid)
) engine=INNODB ;


2��
-- ��ע�͡�ɾ�����ݿ�
DROP DATABASE IF EXISTS mypythondemo
-- ��ע�͡��������ݿ�
CREATE DATABASE mypythondemo CHARACTER SET UTF8
-- ��ע�͡�ʹ�����ݿ�
use mypythondemo
-- ��ע�͡��ж�user���Ƿ���ڣ�������������ɾ��
DROP TABLE IF EXISTS test;
-- ��ע�͡�����user��ͬʱΪÿһ��������˵����Ϣ
CREATE TABLE test(
	uid BIGINT AUTO_INCREMENT COMMENT '�����У��Զ�������',
	name VARCHAR(30) COMMENT '�û�����' ,
	age INT COMMENT '�û�����' ,
	birthday DATE COMMENT '�û�����' ,
	salary FLOAT COMMENT '�û���н' ,
	note TEXT COMMENT '�û�˵��' ,
	CONSTRAINT pk_uid PRIMARY KEY(uid)
) engine=INNODB ;
INSERT INTO test(name,age,birthday,salary,note) VALUES ('�²�',20,'2008-08-13',8000.00,'www.baidu.com');
INSERT INTO test(name,age,birthday,salary,note) VALUES ('������',10,'2007-08-13',9000.00,'www.baidu.com');
INSERT INTO test(name,age,birthday,salary,note) VALUES ('������',28,'2006-08-13',6000.00,'www.baidu.com');



3��
-- ��ע�͡��ж����ݱ��Ƿ���ڣ�������������ɾ��
DROP TABLE IF EXISTS dept ;
DROP TABLE IF EXISTS company ;
-- ��ע�͡��������ݱ��ͬʱΪÿһ��������˵����Ϣ
CREATE TABLE company(
	cid		VARCHAR(20) 		COMMENT '�����У�����ĸC��ͷ��',
	cname	VARCHAR(50) 		COMMENT '��˾����' ,
	site		VARCHAR(200)		COMMENT '��˾��ַ' ,
	CONSTRAINT pk_cid PRIMARY KEY(cid)
) engine=INNODB ;
CREATE TABLE dept(
	did		BIGINT		AUTO_INCREMENT 	COMMENT '�����У��Զ�������',
	dname	VARCHAR(50) 						COMMENT '��������' ,
	cid		VARCHAR(20)						COMMENT '��˾��ţ���Ӧcompany.cid' ,
	CONSTRAINT pk_did PRIMARY KEY(did),
	CONSTRAINT fk_cid FOREIGN KEY(cid) REFERENCES company(cid) ON DELETE CASCADE
) engine=INNODB ;
-- ��ע�͡������׷�Ӳ�������
INSERT INTO company(cid,cname,site) VALUES ('C-001', '����ͯȤ�Ƽ���˾', 'www.kidhalo.com') ;
INSERT INTO dept(dname,cid) VALUES ('��ѧ����', 'C-001') ;
INSERT INTO dept(dname,cid) VALUES ('�̲��з���', 'C-001') ;
INSERT INTO dept(dname,cid) VALUES ('������̲�', 'C-001') ;
-- ��ע�͡��ύ����
COMMIT ;
