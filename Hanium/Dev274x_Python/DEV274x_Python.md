# Python with Jupyter Notebook
Microsoft: DEV274x D.SW기초.3-Introduction to Python: Fundamentals  

-------------
### Module 1 : Sequence Index
##### Using Jupyter
  - 강의는 Azure Notebook 사용법에 대한 내용이나, Azure Notebook Preview가 곧 종료됨에 따라, Jupyter Notebook을 사용해서 실습 진행
  - 2 type cell: code, markdown
  - 단축키 모음 [링크](https://dbrang.tistory.com/1174)

##### String Sequences
  - 문자열은 인덱스를 통해 접근할 수 있음
  - 인덱스는 0부터 시작
  - 음수 인덱스: `맨 뒤 인덱스 = -1`, 앞으로 올수록 `인덱스 += (-1)`

##### Index Slicing
  - substring을 읽을 수 있음
  - `[start : end]`
    - end index 직전까지만 포함(end index는 미포함)
    - 예시) *str[0:2]*
  - `[ : end]`
    - 앞 인덱스를 공백으로 둠으로서, 0을 생략할 수 있음
    - 예시) *str[:2]* 는 *str[0:2]* 와 같음
  - `[start : ]`
    - 뒤 인덱스를 공백으로 둠으로서, stop value를 생략할 수 있음
    - 예시) *str[2:]* 는 *str[2]부터 맨 끝까지 자른 substring*
  - `[ : ]` -> 전체 문자열 반환
  - `[start : end : step]``
    - start index부터 end index까지 step만큼의 칸을 주기로 문자를 가져와서 반환
    - 예시) *print("Colette"[::2]) -> Clte*
    - 예시) *print("Colette"[1::2]) -> oet*
    - 예시) *print("Consequences"[1:9:2]) -> osqe*
  - ```[ : : -1]```
    - 음수 step은 역방향 문자열을 반환
    - 예시) *print("characteristics"[::-1]) -> scitsiretcarahc *
    - 예시) *print("characteristics"[6::-1]) -> tcarahc*

##### Iterating Strings
  - `for --- in ---`
  - ```for (iterator) in (string)```
    - iterator(변수)는 문자열의 한 문자를 가리킴
    - 문자열의 시작에서 끝까지 반복
  - ```for (iterator) in (substring)```
    - 예시) *for i in "hello"[::-1]: print(i) -> olleh*

##### String Method
  - ```len()```
    - 문자열의 길이를 반환
    - 예시) *len("hello hello") -> 11*
  - ```.count()```
    - 원하는 문자/문자열이 몇 번 나타났는지를 반환
    - 예시) *"good code is commented code".count("o")) -> 5*
    - 예시) *print("good code is commented code".count("code")) -> 2*
  - ```.find()```
    1. 원하는 문자가 처음 발생한 위치(인덱스)를 반환
      - 원하는 문자가 발생하지 않으면 -1을 반환
      - 예시) *"save your code".find(" ")) -> 4*
      - 예시) *"good code has meaningful variable names".count("code")) -> 5*  
    2. 두번째 발생한 위치를 알기 위해서는
      - 예시)  
          ```Python
  work_tip = "good code has meaningful variable names"
  # keeps looping until location = -1 (no "o" found)
  while location >= 0:
      print("'o' at index =", location)  
      # find("o", location + 1) looks for a "o" after index the first "o" was found  
      location = work_tip.find("o", location + 1)  
  print("no more o's")
          ```
          ```
  work_tip: good code has meaningful variable names
  'o' at index = 1
  'o' at index = 2
  'o' at index = 6
  no more o's
          ```
    3. ```.find(string, start index, end index)```
      - str[start:end]에서 원하는 substring의 위치를 반환
      - 반환되는 인덱스 값은 원래 string에서의 substring 위치
      - (잘린 이후의 인덱스값이 아님)
  - etc
    - 문자열내에서 숫자 출력 방법
      - 예시) *print("hello x2 length = ", len("hello hello"))*
    - 반올림해서 문자열 자르기
      - 예시) *mid_tip = int(len("hello")/2)*
      -       *print("hello"[:mid_tip])*

##### Module 1: Required Coding Activity
  - `Module1_Submission.ipynb`
  - `Required_Code_MOD1_IntroPy.ipynb`
  - 아래의 함수를 통해, 문구에서 g이상의 첫 문자를 가진 단어를 대문자로 출력하기 코드 작성
    - print()
    - input() *# 괄호에 "문자열"을 넣으면, input 전에 콘솔에 "문자열"을 출력함*
    - for/in
    - if / elif / else
    - .isalpha() : isalpha함수는 문자열이 문자인지 아닌지를 True,False로 리턴
    - .isdigit() : isdigit함수는 문자열이 숫자인지 아닌지를 True,False로 리턴
    - .upper() / .lower()

  - 예시) *"".count("o")) -> 2*
-------------    
### Module 2 : Sequence Manipulation
##### List Sequences
  - SEQUENCE: LISTS
  - List Creation
    - *myList = ["a", "b", "c"]*
    - *myList = ["a", 0.99, 12]* 이렇게 다른 타입도 섞어서도 사용할 수 있음
  - List Access
    - 인덱스를 통해 요소에 접근할 수 있음
    - 이전에 배운 string과 같이 사용할 수 있음
    ``` python
    myList = ["a", 0.99, 12]
    myList[1] -> 0.99
    myList[-1] -> 12
    ```

##### List Append
  - .append() 함수
  - 이전에 만들어진 함수를 통해, 리스트의 끝에 item을 추가할 수 있음
  - 이미 리스트에 들어있는 값이라도, 리스트의 끝에 새로운/중복된 값을 추가 가능
    ``` python
  before: *myList = ["a", 0.99, 12]*
  append: *myList.append("helloWorld")*
  after: *myList = ["a", 0.99, 12, "helloWorld"]*
  ```

##### List Insert / Modify
  - Modify
    - 인덱스를 통해 값을 교체/재할당 할 수 있음
    - *myList[1] = 13*
    - 그러나 인덱스 양이 충분하지 않을 때에는 오류 발생 (out of range)
    - 이미 존재하는 인덱스에 대해서만 사용가능
  - Insert
    - .insert(삽입위치index, 삽입값value)
    ``` python
    before: *myList = ["A", "C", "D"]*
    insert: *myList.insert(1, "B")*
    after: *myList = ["A", "B", "C", "D"]*
    ```
    - 삽입위치에 해당하는 인덱스에 지정한 삽입값이 들어가고, 이후의 값들의 인덱스는 하나씩 뒤로 밀림
    ``` python
    before: *myList = ["A", "C", "D"]*
    insert: *myList.insert(10, "B")*
    after: *myList = ["A", "D", "C", "B"]*
    ```
    - 만약 최대 인덱스를 벗어난 경우, 그냥 맨 뒤에 추가됨

##### List Delete
  - `del`
    - 리스트 인자를 인덱스를 통해 지울 수 있음
    - `del myList[0]` 식으로 처음 원소를 지울 수 있음
    - `del myList[-1]` 식으로 마지막 원소를 지울 수 있음
  - `.pop()`
    - 리스트의 맨 뒤 원소를 반환하고, 리스트의 맨 뒤 원소를 지움
    - *return, remove* last item
    ``` python
    print(myList.pop())
    print(myList.pop(3)) // 3번째 인덱스를 return, remove
    ```
    - list가 비어있는 상태에서 pop을 진행하게 되면, false를 return
    ``` Python
    while myList:
        print(myList.pop()) # 활용법
    ```
  - `.remove()`
    - value를 통해 원소를 제거할 수 있음
    - `del`, `pop()`은 인덱스를 통해 원소를 제거
    - `remove()`는 원소값을 통해 원소를 제거
    - *myList.remove("dog")* 와 같은 방식으로 제거
    ``` python
    myList = ['b', 'b', 'a', 'b', 'c']
    while 'b' in myList:
          myList.remove('b')
    # 'b'가 더이상 리스트에 존재하지 않을때까지 반복
    # 맨앞의 'b'를 지우고 다시 while문을 시작, 다시 맨앞의 'b'를 지우는 것을 반복
    # ~until 'b'가 더이상 리스트에 존재하지 않을때까지.
    ```
    - 존재하지 않는 item을 remove하고자하면, ValueError 발생

##### Module 2: Required Coding Activity
  - `Module2_Submission.ipynb`
  - `Required_Code_MOD2_IntroPy.ipynb`
  - 아래의 함수를 통해, 프로그램 구현
  - 리스트가 비어있으면 종료
  - 리스트가 비어있지 않으면 문자열 입력을 받음
  - 문자열이 리스트에 이미 있는 원소라면, 해당 원소를 제거 remove()
  - 리스트에 없는 원소라면, 리스트에 문자열을 추가 append()
  - 문자열이 공백일 때는 맨 마지막 원소를 pop()
    - def
    - in
    - return
    - print()
    - input()
    - .append()
    - .pop()
    - .remove()
    - if

  - 예시) *if "horse" in myList: ~~~*
  *잘 구현했는데, 왜 틀렸다고 뜰까... grade 1점 못받아서 속상하다*

-------------    
### Module 3 : Sequence Iteration
##### Power of List Iteration (for in)
  - for in
    - `for 변수 in 리스트:` : 변수에 리스트의 원소를 앞에서부터 차례대로 넣음
    - sort & filter: 다른 함수와 결합하여, 원하는 정보를 걸러서 처리할 수 있게 함
    - count & search
      - count
      ``` Python
      myList = ["abca", "aaaa"]
      for var in myList:
        cnt += var.lower().count('a') # a가 리스트에 몇개 들어가는지 확인
      # 이 방법이, 대소문자 가리지 않고 개수 세는 방법에 최적인듯!
      # count() : string에 substring이 몇 번 들어가는지 반환
      # 7
      ```
      - search
      ``` python
      for var1 in myList:
        if var1.lower() == var2.lower(): # 전체 문자열이 같은지 확인
          return True
        if var1.startswith("P"):  # San Paulo : False
          return True
      ```

##### Range Iteration (for in range)
  - for in range
    - range(stop)
      - `range(10)` == `range(0, 10)` == {0, 1, 2,..., 8, 9}
      - 0부터 stop 조건 미만 반복
      - 활용가능: *myList(range(10))* == *[0,1,2,3,4,5,6,7,8,9]*
      - `for var in range(10): ` # 10회 반복
    - range(start, stop)
      - start <=  < stop
      - `range(5, 10)` == {5, 6, 7, 8, 9}
    - range(start, stop, step)
      - step 만큼 더해가며 반복
      - 조건: start <=  < stop
      - `for var in range(25, 101, 25): print(var)` == {25, 50, 75, 100}
    > for 변수 in range( , , ) :   # 이런식으로 사용

##### extend, reverse, sort methods
  - .extend()
    - 문자열 합치기
    - `str1.extend(str2)` == `str1 + str2`
    - cf) `list1 + list2` : *리스트끼리 합칠 수 있음, list1뒤에 list2가 붙음*
  - .reverse()
    - `myList.reverse()` : 순서를 반전시킴. 리턴없음
  - .sort()
    - `myList.sort()` : 오름차순(알파벳) 정렬. 리턴없음
    - `sortedList = sorted(myList)` : 오름차순으로 정렬된 리스트를 반환함. 인자로 받는 리스트는 변경되지 않음.
  > 기존의 인자를 변경하지않는 것은 sorted() 함수

##### between strings & lists
  - string to lists: .split()
  - list to strings: .join()

-------------    
### Module 4 : Files

##### files import, open & read
  - jupyter notebook에서 파일 import하기
    - `!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/poem1.txt -o poem1.txt`
      - !	: runs command interface supporting curl
      - curl :	enables curl that can download files
      - https://raw.githubusercontent.com/... :	is the address for data file to import
      - -o :	tells curl write data to a file
      - poem1.txt :	name curl will give the file
  - open file
    - `fd = open('file.txt', 'r')` : read only mode
      - fd는 파일의 정보를 가지고있음
      - 두번째 인자를 통해 모드 지정 가능
        - 'r'	: read only mode
        - 'w'	: write - overwrites file with same name
        - 'r+' : read and write mode
        - 'a'	: opens for appending to end of file
  - read file
    - `contents = fd.read()` : 파일 내용을 읽어와서 변수에 저장
      - open 이후에 사용 가능
      - 문자열을 반환
      - 파일 내용을 일반 문자열, 변수처럼 다룰 수 있게 됨
    - `contents = fd.read(10)` : 처음 10글자를 읽어와서 반환
      - 첫 10글자를 읽은 이후에 포인터는 11번째 글자에 가 있으므로 다음 read 함수를 호출하면 11번째 글자부터 나옴
    - fd.read().func()
      - read()는 문자열을 반환하기 떄문에
      - -> func(): 문자열에 사용되는 함수를 그대로 사용할 수 있음
      - upper(), lower()
      - title() : 각 단어의 첫 글자를 대문자로 변경
      - isalpha(), isdigit()
      - [10: 20] // slicing

##### file .readlines and .close() methods
    - .readlines() method
      - : open text as list (텍스트파일을 문자열 리스트로 바꿀 수 있음)
      - `lists = fd.readlines()`
        - 각각 newline을 breakpoint로 가지는 문자열이 리스트를 이룸
        - file open 이후에 바로 사용 가능
      - 맨 뒤에 '\n'을 포함
        - 각 문자열의 마지막 char는 '\n'
        - []'hello\n', 'world\n', ...] 이런식으로 이루어져있음
      - 각 item에서 '\n'을 지우는 법
        - string slicing을 이용
        - `line[:-1]` // 마지막 char을 포함하지 않겠다는 것
          ```Python
          count = 0
          for line in lists:
            lists[count] = line[:-1]
            count += 1
          ```
    - .close() method
      - open file은 메모리를 사용하므로 close를 통해 memory(resource)를 free해주어야함
      - `fd.close()`
      - close 이후에 read하려하면 IO Exception 오류 발생

##### file .readline and .strip() methods
  - .readline()
    - 파일을 한줄씩 읽기 위해서 사용
    - 한줄을 읽고 난 이후에는 포인터가 다음줄 첫 문자로 옮겨감
    - 따라서 다음 순서에는 다음 줄부터 읽을 수 있음
    - '\n'을 마지막 문자로 가지고 있음(readlines와 동일하게...)
  - .readline() while loop
    - 반복문을 사용하여 한 iter당 파일 내용 한 줄씩 가져올 수 있음
    - 포인터가 끝을 가리키면 readline()은 빈 문자열을 반환
    - 처음부터 다시 읽기위해서는 파일을 닫고 다시 열어야함
      ``` Python
      line = fd.readline() # 이거 없으면 line 변수에 대한 형식을 찾지 못함
      while line:
        print(line[:-1].upper())
        line = fd.readline()
      ```
  - .readline() with .strip()
    - 공백 지우기
    - `line = fd.readline().strip()` : 앞뒤의 공백, 개행을 지워줌
  - .strip() method arguments
    - `"**Yel*low**\n".strip('*\n')` == `"Yel*low"`
    - default로 문자열의 앞뒤 공백과 개행을 삭제
    - 인자로 문자열을 주면, 해당 문자들을 문자열의 앞뒤에서 삭제
    - 중간의 문자는 삭제하지 않음. 맨 앞/뒤에만 적용

##### write() & .seek() methods
    - w' or 'w+' modes
      - 텍스트파일을 생성하거나 수정(오버라이팅, 이전 데이터 삭제) 가능
      - 'w' : write mode
      - 'w+' : read + write mode
      - `fd = open('file.txt', 'w')`
    - .write()
      - `fd.write("hello\nworld\n")`
      - 파일에 쓴 글자수를 반환
      - file write 이후에 포인터는 파일의 맨 끝에 위치
    - .seek(0) method
      - 파일 포인터를 옮길때 사용
      - 파일을 닫고 다시 여는 것이 아닌, 파일 포인터만 옮길 수 있음
    - .seek() offset & whence
      - file.seek(char offset, optional whence)
      1. `file.seek(offset)`
        - : `file.read()[offset:]`에 해당하는 문자열을 가지고오게 됨
      2. whence mode: 어디서부터 오프셋 수를 셀 지
        - 0: points offset to the beginning of the file
        - 1: points offset from current location
        - 2: points to the end of the file & offset is always 0
      ```Python
      # 파일의 마지막 줄에 write 가능
      fd.seek(0, 2) # end of file을 의미
      fd.write("the last line! \n")

      # 파일의 첫 줄을 오버라이팅
      fd.seek(0)
      fd.write("the first line! \n")
      ```
    - writable modes
      - : 'w', 'w+', 'r+', 'a', 'a+'
      - MODE	Description
        - 'r'	read only mode
        - 'r+'	read and write mode (no overwrite). 추가하여 쓰기만 가능(seek 2 옵션 사용)
        - 'w'	write - overwrites file with same name
        - 'w+'	write and read mode - overwrites file with same name
        - 'a'	opens for appending to end of file (no overwrite)
        - 'a+'	opens for appending to end of file (no overwrite) plus read
        - **#주의** *'w', 'w+': 파일이 없으면 새로운 파일을 만들어서 쓰고, 파일이 존재하면 기존 내용을 삭제하고 오버라이팅*

> EOL while scanning string literal : 발생 이유. 프로그램 구문이 잘못 쓰였을 때


-------------    
### Module 5 : Final Evaluation
