우분투 글타레 https://forum.ubuntu-kr.org/viewtopic.php?f=4&t=23407

톰보이 웹서비스(Tomboy Web Service)
 
- 톰보이의 '동기화'파일들을 웹상에서도 읽고, 편집할수 있게 해주는 서비스입니다.
- php와 python, 자바스크립트로 구성되어져 있습니다.
- 웹상에서 문서를 편집할때 사용된 에디터는 uix님의 이지웹 에디터를 사용하였습니다. 이렇게 간단하고 쉬운 에디터를 쓸 수 있게 공개해주신 uix님께 감사의 말씀 드립니다.
  (http://uix.kr/service)
- 톰보이에서 사용하는 '동기화' 폴더를 싱크할수 있도록 하면 사용이 가능해집니다. 톰보이에서 동기화폴더를 지정하시어 동기화를 거신 뒤에 그 폴더를 '톰보이 웹 서비스'폴더 내에 'notefile'이라는 제목으로 심볼릭 링크를 걸어주신 뒤에 사용하시면 됩니다.(단, 웹서비스 폴더와 동기화 폴더 모두 sudo chmod -R 666*를 주서야 할 것입니다)

현재 구현되는 기능은
- 톰보이와 웹 간의 동기화
- 타이틀 검색을 통한 바로 가기
- 쪽지 편집
- 새 쪽지 생성
- 쪽지 저장시 내용 안에 '타이틀'과 동일한 키워드가 존재할 시에 '링크' 생성
(단, '키워드' 앞 뒤로 스페이스(' ')가 있어야 가능합니다.


주의사항은
- Seony님의 지적대로 php로 python을 구현하게 한 것이기 때문에, 보안이 좋지 못합니다.
- 보이지 않은(?) 수많은 버그들이 존재합니다.
- 톰보이에서는 메모 동기화시에 manifest에 기재된 파일중 '하나'라도 없을 시에 동기화 실패로 넘어가는데, 아직 이에 대한 대비기능이 없습니다.
- 쪽지를 불러오는 방식이 GET 방식인데, 이를 아스키로 변경해주질 않아서 아직 타이틀 내에 '특수문자' 삽입을 할수 없습니다.

- This SERVICE is helping people to read and edit 'tomboy synced file' on web.
- 'php', 'python', 'JavaScript' are used in this SERVICE.
- Specially, thanks to 'uix' who shared 'EAZY WEB EDITOR'. It made the SERVICE peossible to edit the text on web.(http://uix.kr/service)
