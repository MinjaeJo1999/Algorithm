#include <iostream>
#include <vector>

using namespace std;
vector<int> arr;

void bubbleSort(int n){
    //오름차순
    //순서대로 비교 반복
    int cnt = 0;
    for(int i=1; i<n; i++){
        for(int j=1; j<=n-i; j++){ //비교해야 할 인접 원소가 하나씩 줄어듦
            if(arr[j]<arr[j-1]){ //인접한 두 원소 비교 , 오름차순 아니면 자리 교환
                int temp;
                temp = arr[j];
                arr[j] = arr[j-1];
                arr[j-1] = temp;
            }
        }
    }
}

//향상된 버블 정렬 : 정렬 완료되면 종료 / 이미 정렬된 경우 정렬 카운트 단축
//(출처 : 1기 알튜비튜 풀이 코드)
void bubbleSortAdv(int n){

    for (int i = 0; i < n; i++) {
        bool flag = true;
        //0 ~ n-1까지 정렬 -> 0 ~ n-2까지 정렬 -> ... -> 0 ~ 1까지 정렬
        for (int j = 1; j < n - i; j++) {
            if (arr[j - 1] > arr[j]) {
                flag = false;
                swap(arr[j - 1], arr[j]); //swap 함수
            }
        }
        //출력할게 아니라면 return 으로 수정해도 됨
        if(flag)
            break;
    }
}



int main(){
    int n;
    cin >> n;
    arr.assign(n,0);
    for(int i=0; i<n; i++) {
        cin >> arr[i];
    }
    bubbleSort(n);
    //bubbleSortAdv(n);
    for(int i=0; i<n; i++) {
        cout << arr[i] << '\n';
    }
    return 0;
}


/*주의*/
//배열 크기만큼 할당 해주어야 : arr.assign(n,0);
//for문 조건 = 유무: j<=n-i
//함수 리턴 타입 지정 잘못해서 컴파일 에러: void bubbleSort

