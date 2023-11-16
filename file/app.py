from flask import Flask, render_template, request, redirect, url_for, session
import db, string

app = Flask(__name__)

@app.route('/', methods=['GET'])
def request():   
    return render_template('request.html')
    
@app.route('/', methods=['POST'])
def request_exe():
    club_name = request.form.get('club_name')
    leader_mail = request.form.get('leader_mail')
    objective = request.form.get('objective')
    activities = request.form.get('activities')
    introduction = request.form.get('introduction')
    note = request.form.get('note')
    allow = request.form.get('allow')

    if db.request(club_name, leader_mail, objective, activities, introduction, note, allow):
        session['user'] = True # session にキー：'user', バリュー:True を追加
        return redirect(url_for('request'))
    else :
        error = '申請に失敗しました。'
        return render_template('request.html', error=error)

@app.route('/')
def approve():
    return render_template('approve.html')

@app.route('/approve_exe', methods=['POST'])
def qpprove_exe():
    club_name = request.form.get('club_name')
    leader_mail = request.form.get('leader_mail')
    objective = request.form.get('objective')
    activities = request.form.get('activities')
    introduction = request.form.get('introduction')
    note = request.form.get('note')
    allow = request.form.get('allow')
    
    count = db.insert_user(club_name, leader_mail, objective, activities, introduction, note, allow)
    
    if count == 1:
        msg = '承認しました。'
        return redirect(url_for('approve_succes', msg=msg))
    else:
        error = '否認しました。'
        return render_template('approve.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)