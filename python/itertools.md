# itertools
현재 브루트 포스 알고리즘을 푸는데, itertools를 사용하면 너무 간단히 풀리는 문제들이 많아서 사용법을 정리하고자 한다!

### 목차
1. [조합 : `combinations`](#1-조합---combinations)
2. [중복조합 : `combinations_with_replacement`](#2-중복조합---combinations_with_replacement)
3. [순열 : `permutations`](#3-순열---permutations)
4. [중복순열 : `product`](#4-중복순열---product)


## 1. 조합 - `combinations`
- 반복 가능한 길이가 n인 객체에 대해서, **중복을 허용하지 않고 r개를 뽑는다.**
- 어떤 것을 뽑는지만 중요하게 보기 때문에 뽑는 순서는 고려하지 않는다. (순서에 의미가 없다.)
- 🚨🚨**주의 : `combinations(arr, r)` 에서 len(arr) < r 이면 빈 배열을 반환한다!!!**🚨🚨
- <sub>n</sub>C<sub>r</sub> = `combinations(arr, r)`


## 2. 중복조합 - `combinations_with_replacement`
- 반복 가능한 길이가 n인 객체에 대해서, **중복을 허용하고 r개를 뽑는다.**
- <sub>n</sub>H<sub>r</sub> = <sub>n+r-1</sub>C<sub>r</sub> = `combinations_with_replacement(arr, r)`


## 3. 순열 - `permutations`
- 반복 가능한 길이가 n인 객체에 대해서, **중복을 허용하지 않고 r개 뽑아서 나열한다.**
- 뽑힌 순서대로 나열한다. 순서에 의미가 있다.
- 같은 값이 뽑히더라도 순서가 다르면 다른 경우의 수로 취급한다.
- <sub>n</sub>P<sub>r</sub> = `permutations(arr, r)`


## 4. 중복순열 - `product`
- 반복 가능한 길이가 n인 객체에 대해서, **중복을 허용하고 r개 뽑아서 나열한다.**
- <sub>n</sub>∏<sub>r</sub> = `product(arr, repeat)` = n<sup>r</sup>