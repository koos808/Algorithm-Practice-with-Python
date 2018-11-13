""" 3.캐시 - 난이도 : 하
지도개발팀에서 근무하는 제이지는 지도에서 도시 이름을 검색하면 해당 도시와 관련된 맛집 게시물들을 데이터베이스에서 읽어 보여주는 서비스를 개발하고 있다.
이 프로그램의 테스팅 업무를 담당하고 있는 어피치는 서비스를 오픈하기 전 각 로직에 대한 성능 측정을 수행하였는데, 제이지가 작성한 부분 중 데이터베이스에서 게시물을 가져오는 부분의 실행시간이 너무 오래 걸린다는 것을 알게 되었다.
어피치는 제이지에게 해당 로직을 개선하라고 닦달하기 시작하였고, 제이지는 DB 캐시를 적용하여 성능 개선을 시도하고 있지만 캐시 크기를 얼마로 해야 효율적인지 몰라 난감한 상황이다.

어피치에게 시달리는 제이지를 도와, DB 캐시를 적용할 때 캐시 크기에 따른 실행시간 측정 프로그램을 작성하시오.

#입력 형식
캐시 크기(cacheSize)와 도시이름 배열(cities)을 입력받는다.
cacheSize는 정수이며, 범위는 0 ≦ cacheSize ≦ 30 이다.
cities는 도시 이름으로 이뤄진 문자열 배열로, 최대 도시 수는 100,000개이다.
각 도시 이름은 공백, 숫자, 특수문자 등이 없는 영문자로 구성되며, 대소문자 구분을 하지 않는다. 도시 이름은 최대 20자로 이루어져 있다.

#출력 형식
입력된 도시이름 배열을 순서대로 처리할 때, “총 실행시간”을 출력한다.

#조건
캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
cache hit일 경우 실행시간은 1이다.
cache miss일 경우 실행시간은 5이다.

#인사이트
LRU라는건 캐시에서 디스크에 있는 데이터를 미리 가져다 놓은 상태에서 캐시 미스가 날 경우

가장 오래전에 사용된것 ==  Least Recently Used == 가장 최근에 덜 사용된 것을 캐시에서 내보내고 새로운 데이터를 캐시에 올려놓는다.



"""

#참조 CODE 1

def question3(cache_size, cities):
    exe_time = 0
    cache = []
    if cache_size == 0:
        return len(cities)
    else:
        for i in range(0, cache_size):
            cache.append("")

    for c in cities:
        is_hit = False
        for i in range(0, cache_size):
            if cache[i].lower() == c.lower():
                temp_str = cache[i]
                for j in range(i, 0, -1):
                    cache[j] = cache[j -1]
                cache[0] = temp_str
                is_hit = True
                break
        if is_hit:
            exe_time += 1
        else:
            exe_time += 5
            for i in range(cache_size -1, 0, -1):
                cache[i] = cache[i - 1]
            cache[0] = c
    return exe_time


print( question3(3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']) )



# 참조 CODE 2
def LRUtime(cachesize, cities):
    if cachesize < 0  or cachesize > 30:
        print("cachesize는 0~30사이로 입력하세요.")
        return

    if len(cities) > 100000:
        print("도시 갯수는 최대 10,000개 입니다.")
        return

    # 작업 변수 정의
    cache = []
    time_cache_hit  = 1
    time_cache_miss = 5
    run_time        = 0

    for city in cities:
        city_str = city.upper()

        # Caching작업 : LRU(Least Recently Used)
        if city_str in cache:
            cache.remove(city_str)
            cache.append(city_str)
            run_time += time_cache_hit
        elif cachesize > 0:
            if len(cache) == cachesize:
                del cache[0]
            cache.append(city_str)
            run_time += time_cache_miss
        else: # cachesize가 0일때는 Caching작업 안함
            run_time += time_cache_miss
    return run_time

print( LRUtime(3,['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']) )
