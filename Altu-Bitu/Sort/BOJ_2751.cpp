//백준 : 수 정렬하기 2
//링크 : https://www.acmicpc.net/problem/2751

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector <int> arr;
vector <int> ans;


//ex)
// 4 3 6 1
// 4 , 3 / 6, 1

void mergeSort(int left, int mid, int n){
    int p1 = left;
    int p2 = mid+1;
    int p3 = left; //ans 인덱스용

    //알고리즘 헤더
    sort(arr.begin(), arr.begin()+(mid+1));
    sort(arr.begin()+mid, arr.begin()+n);

    while(p1 <=mid && p2<n){
        if(arr[p1] <= arr[p2] ){
            ans[p3++] = arr[p1++];
           // cout << "Left insert: " << arr[p1-1] << '\n' ;
        }
        else {
            ans[p3++] ==  arr[p2++];
           // cout << "Right insert: " << arr[p2-1] << '\n';
        }
    }
    if(p1 < mid){
        while(p1 <= mid){
            ans[p3++] = arr[p1++];
        }
    }
    if(p2 < n-1){
        while(p1 < n-1){
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
// 탐색하지 않은 원소도 고려