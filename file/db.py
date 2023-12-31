import os, psycopg2, string, random, hashlib

def get_connection():
    url = os.environ['DATABASE_URL']
    connection = psycopg2.connect(url)
    return connection

def request_club(club_name, leader_mail, objective, activities, introduction, note, allow):
    sql = 'INSERT INTO club VALUES (default, %s, %s, %s, %s, %s, %s, %s)'

    try : # 例外処理
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (club_name, leader_mail, objective, activities, introduction, note, allow))
        count = cursor.rowcount # 更新件数を取得
        connection.commit()
        
    except psycopg2.DatabaseError: # Java でいうcatch 失敗した時の処理をここに書く
        count = 0 # 例外が発生したら0 をreturn する。
    
    finally: # 成功しようが、失敗しようが、close する。
        cursor.close()
        connection.close()
    
    return count

def approve(club_id, club_name, leader_mail, objective, activities, introduction, note, allow):
    sql = 'SELECT * from club'
    flg = False
    try :
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(sql, (club_id, club_name, leader_mail, objective, activities, introduction, note, allow))
        user = cursor.fetchone()
        
    except psycopg2.DatabaseError :
        flg = False
    finally :
        cursor.close()
        connection.close()
    return flg