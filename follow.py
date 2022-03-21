
# skype: live:.cid.25774c9be2083ed2

import os
import requests
proxies = False

cookies = {
    'install_id': '7065961268208781062',
    'passport_csrf_token': '62047aa6648fb29aae9c52df433c8996',
    'passport_csrf_token_default': '62047aa6648fb29aae9c52df433c8996',
    'd_ticket': 'a6d598d4aa88b5d4fd6c2c375500f58ed53a8',
    'multi_sids': '7033846646693856261%3A201a43e53bd2cd7aaeec7349ca77d867',
    'cmpl_token': 'IGNORE',
    'odin_tt': '80642a77393520d994aa7158c1e9f586b49619588bf8320faa52c18f5ba4f0b9c00bbfd79652140d810be05d2d2f1cc1372c4c86eec36170cc2cf9a14a00e87f',
    'sid_guard': '79bbdf15cfc09bcf4690efe5719ad79b%7C1637092729%7C5183999%7CSat%2C+15-Jan-2022+19%3A58%3A48+GMT',
    'uid_tt': 'fb311e9c660ae48baaa88e7105661ecd23a858f78764908107df0e45cc5ede18',
    'uid_tt_ss': 'd45cf06f1de2a2b05fa63e77484585429f19c76f03cad6642a7485d7c8d94549',
    'sid_tt': '79bbdf15cfc09bcf4690efe5719ad79b',
    'sessionid': '79bbdf15cfc09bcf4690efe5719ad79b',
    'sessionid_ss': '79bbdf15cfc09bcf4690efe5719ad79b',
    'store-idc': 'alisg',
    'store-country-code': 'tr',
    'msToken': 'ZV0QTcCgZDNXQNqHg4GlWs82dO6g5hsxn50usgZyM7sZYVW31wDA-Rz0qskNY-Rjr8l93FS0sYyJWwtQWGe1meXKCaqcOMv1IXOlOC-21s0=',
    # 'install_id': '7065961268208781062',
    # 'passport_csrf_token': '62047aa6648fb29aae9c52df433c8996',
    # 'passport_csrf_token_default': '62047aa6648fb29aae9c52df433c8996',
    # 'd_ticket': 'a6d598d4aa88b5d4fd6c2c375500f58ed53a8',
    # 'multi_sids': '7033846646693856261%3A201a43e53bd2cd7aaeec7349ca77d867',
    # 'cmpl_token': 'IGNORE',
    # 'odin_tt': '7074acff983aa7eec00c3f2a51f6acbb34bf42860d3584f29c4daf98b2b37d8d8e457015fd4a73fb349922c9b85a46340e5553226e3918ee781bd8d53331aad45fa10eba2d588fe08ee2f6756c988bab',
    # 'sid_guard': '201a43e53bd2cd7aaeec7349ca77d867%7C1645172492%7C5184000%7CTue%2C+19-Apr-2022+08%3A21%3A32+GMT',
    # 'uid_tt': 'd45cf06f1de2a2b05fa63e77484585429f19c76f03cad6642a7485d7c8d94549',
    # 'uid_tt_ss': 'd45cf06f1de2a2b05fa63e77484585429f19c76f03cad6642a7485d7c8d94549',
    # 'sid_tt': '201a43e53bd2cd7aaeec7349ca77d867',
    # 'sessionid': '201a43e53bd2cd7aaeec7349ca77d867',
    # 'sessionid_ss': '201a43e53bd2cd7aaeec7349ca77d867',
    # 'store-idc': 'alisg',
    # 'store-country-code': 'ge',
    # 'msToken': 'ZV0QTcCgZDNXQNqHg4GlWs82dO6g5hsxn50usgZyM7sZYVW31wDA-Rz0qskNY-Rjr8l93FS0sYyJWwtQWGe1meXKCaqcOMv1IXOlOC-21s0=',
}

headers = {
    'Host': 'api16-normal-c-useast1a.tiktokv.com',
    'passport-sdk-version': '19',
    'sdk-version': '2',
    'x-tt-multi-sids': '7033846646693856261%3A201a43e53bd2cd7aaeec7349ca77d867',
    'x-tt-token': '01201a43e53bd2cd7aaeec7349ca77d867052ad284e7e578c256193fc5881a83e582ad048100ca4c54eb176be5f3d18e59cd39bb3d0e718da2c65601a1009930c236d53ef56fe3d0e207e50fdd4578a2ac880fc1ab53b96096c7a70fdef3b7d0de282-1.0.1',
    'multi_login': '1',
    'x-ss-req-ticket': '1645172860990',
    'x-vc-bdturing-sdk-version': '2.2.1.i18n',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'x-tt-cmpl-token': 'IGNORE',
    'x-tt-store-idc': 'alisg',
    'x-tt-store-region': 'ge',
    'x-tt-store-region-src': 'uid',
    'user-agent': 'com.zhiliaoapp.musically/2022301040 (Linux; U; Android 7.1.2; en_US; G011A; Build/N2G48H;tt-ok/3.10.0.2)',
    'x-ladon': 'MwhocSqZr2QFWaSNFIdwDMrcToPqIYOsXZmkXNJgjQBXP3nJ',
    'x-gorgon': '040440a600007640148c4ce7272b9ec63a883f1817d91ee9794e',
    'x-khronos': '1645172860',
    'x-argus': 'XAfVc+RmCurgfygSlXn5jr596rGoQ3s6Qmlp68FoUB22UAX6ESpnHTqQVTEsw3fFtLXnU4mj/otRmmMdGXyqF20H17izy5/Vm8IIlfcdXI+TUDbqqWCLh17jajwxnzZjJXc5cUk0tQnUtKSqD99mtwGVgPAC4x5niSQy5htP4iK8NpH76Ju09G5k9lJF0DSSVIA7z7HclnGn/1JXwySZeeGPT5OpEIv8btxtFE6cwKRvmj920n+KHAnFBC9wAn4tUchJ0vmhlg5YJWnZBzSPJGe5rtiOVZUVyPygbDhw+HJgCw==',
}

response = requests.get('https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/commit/follow/user/?link_sharer=0&channel_id=23&from_pre=-1&from=14&sec_user_id=MS4wLjABAAAAG3Dgd55l3j81sb3Hv5FI6I-rBPnAaeeSuG1K_8w2Dx4ChtBEJhFkL2Gm3KELMqWB&type=1&city&iid=7065961268208781062&device_id=6985408846991787526&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230104&version_name=23.1.4&device_platform=android&ab_version=23.1.4&ssmix=a&device_type=G011A&device_brand=google&language=en&os_api=25&os_version=7.1.2&openudid=a6e088767ce766cb&manifest_version_code=2022301040&resolution=1080*1920&dpi=360&update_version_code=2022301040&_rticket=1645172860989&current_region=ID&app_type=normal&sys_region=US&mcc_mnc=51010&timezone_name=Asia%2FShanghai&residence=ID&ts=1645172860&timezone_offset=28800&build_number=23.1.4&region=US&uoo=0&app_language=en&carrier_region=ID&locale=en&op_region=ID&content_language=en%2C&ac2=wifi&host_abi=x86&cdid=898723a6-c81b-48c8-804d-e862c5e9d55f', headers=headers, cookies=cookies, proxies=proxies)

print(response.text)
