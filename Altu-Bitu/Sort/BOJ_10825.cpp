//백준 : 국영수
//링크 : https://www.acmicpc.net/problem/10825
//참고 코드 : 알튜비튜 1기 솔루션 코드

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct info {
    string name;
    int korean, english, math;
};


//국어는 내림차순
//영어는 오름차순
//수학은 내림차순
//이름은 오름차순 (아스키 코드 상 대문자 < 소문자)
//메모리 6720 KB , 시간 148 ms
bool cmp(const info &i1, const info &i2){
    if(i1.korean == i2.korean){
        if(i1.english == i2.english){
            if(i1.math == i2.math){
                return i1.name < i2.name;
            }
            return i1.math > i2.math;
        }
        return i1.english < i2.english;
    }
    return i1.korean > i2.korean;
}

//더 나은 버전
//메모리 6720 KB , 시간 148 ms
bool cmpAdv(const info &i1, const info &i2){
    if(i1.korean != i2.korean) return i1.korean > i2.korean;
    if(i1.english != i2.english) return i1.english < i2.english;
    if(i1.math != i2.math) return i1.math > i2.math;
    return i1.name < i2.name;
}


int main(){
    int n;
    vector<info> student;
    cin >> n;
    student.assign(n,{});

    for(int i=0; i<n; i++){
        cin >> student[i].name >> student[i].korean >> student[i].english >> student[i].math;
    }

    sort(student.begin(), student.end(), cmpAdv);

    for(int i=0; i<n; i++){
        cout << student[i].name << '\n';
    }

    return 0;
}


/*주의*/
//구조체 활용
//cin 연속
//함수 대신 sort의 compare 함수 정의
//비교함수 리턴값 bool
//비교함수 인자 const 와 &로 레퍼런스 값 전달
//중첩 반복될땐 scope 내용 잘 확인
//출력까지