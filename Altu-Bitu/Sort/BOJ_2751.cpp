//백준 : 수 정렬하기 2
//링크 : https://www.acmicpc.net/problem/2751

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> arr;
vector <int> ans;

//메모리 9849KB , 시간 668ms
void mergeSort(int left, int mid, int n){
    int p1 = left;
    int p2 = mid;
    int p3 = left; //ans 인덱스용

    //알고리즘 헤더
    sort(arr.begin(), arr.begin()+mid);
    sort(arr.begin()+mid, arr.end());

    //중간 정렬 확인 ( left: 3개 , right: 4개)
  /* for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }
    cout << '\n'; */

    while(p1 < mid && p2<n){
        if(arr[p1] <= arr[p2] ){
            ans[p3++] = arr[p1++];
            //cout << "Left insert: " << arr[p1-1] << '\n' ;
        }
        else {
            ans[p3++] =  arr[p2++];
            //cout << "Right insert: " << arr[p2-1] << '\n';
        }
    }
    if(p1 <= (mid-1)){ //인덱스 초과 방지
        while(p1 <= (mid-1)){
            ans[p3++] = arr[p1++];
        }
    }
    if(p2 <= n-1){ //인덱스 초과 방지
        while(p2 <= n-1){
            ans[p3++] = arr[p2++];
        }
    }
}

int main(){
    int n;
    cin >> n;
    arr.assign(n,0);
    ans.assign(n,0);

    for(int i=0; i<n; i++){
        cin >> arr[i];
    }

    int mid = n/2;
    int left = 0;

    //힙정렬
    mergeSort(left, mid, n);

    //정렬후
    for(int i=0; i<n; i++){
        cout << ans[i] << '\n';
    }

    return 0;
}


/*주의*/
// sort 함수 사용 시 인자는 배열의 주솟값 전달해줘야
// 인덱스 초과 방지 조건 고려해야
// 탐색하지 않은 원소도 고려, 탐색되지 않은 나머지 원소 ans 배열에 삽입해야
// 오른쪽 기준 mid로 할지, mid+1로 할지 결정 후 모든 조건에 통일적으로 반영
// 인덱스 초과 방지 조건에서 '=' 추가해서, 탐색되지 않은 마지막 인덱스 값 배제하지 않도록

/*개선*/
//시간이 너무 오래 걸린다! 어떻게 개선할 수 있을지 생각