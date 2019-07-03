# -*- coding: utf-8 -*-

import re

text = '''
      <div class="seo-recommended-notes">

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/87fd419c94cc?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/6011252-2e9dd73b62bc22d7.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/87fd419c94cc?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">多图万字文 | 从神经元到CNN、RNN、GAN…神经网络看本文绝对够了</a>
              <p class="description">作者 | FJODOR VAN VEEN 编译 | AI100（ID：rgznai100） 在深度学习十分火热的今天，不时会涌现出各种新型的人工神经网络，想要实时了解这些新型神经网络的架构还真是不容易。光是知道各式各样的神经网络模型缩写（如：DCIGN、BiLSTM、DCG...</p>
              <a class="author" target="_blank" href="/u/da69420ec62d?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6011252/7a0a40dc-6ebb-43e2-8cc3-6e4273d0c100.png?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">AI科技大本营</span>
</a>            </div>

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/f054f8daec68?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/6011252-1fe573b6313bd7f6?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/f054f8daec68?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">多图 | 从神经元到CNN、RNN、GAN…神经网络看本文绝对够了</a>
              <p class="description">作者 | FJODOR VAN VEEN 编译 | AI100（ID：rgznai100） 在深度学习十分火热的今天，不时会涌现出各种新型的人工神经网络，想要实时了解这些新型神经网络的架构还真是不容易。光是知道各式各样的神经网络模型缩写（如：DCIGN、BiLSTM、DCG...</p>
              <a class="author" target="_blank" href="/u/da69420ec62d?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6011252/7a0a40dc-6ebb-43e2-8cc3-6e4273d0c100.png?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">AI科技大本营</span>
</a>            </div>

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/d649c842f915?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/8662455-aed689a72818842b?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/d649c842f915?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">从神经元到CNN、RNN、GAN…神经网络集锦</a>
              <p class="description">姓名：周雪宁 学号：1702110196 转载：https://mp.weixin.qq.com/s/Si2jtA3jrKJVCXJ1B3fZQw 【嵌牛导读】：在深度学习十分火热的今天，不时会涌现出各种新型的人工神经网络，想要实时了解这些新型神经网络的架构还真是不容易。光...</p>
              <a class="author" target="_blank" href="/u/6a4d2181680d?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/8662455/3e0e8240-91ce-4993-98ce-ce9f2092e3a0.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">周雪宁</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/701d25b74a7a?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">白茶清欢无别事（上）</a>
              <p class="description">五点钟把闹钟关了。 接下来的十几分钟我做了一个梦。 我记不大清梦的内容。但可以确定的一点是——将来的某一天我会再次经历一遍。原因恰恰在于梦的日常与平淡。我有预感这个将来不会太久，以不至于在岁月流逝中将梦冲刷的干干净净、一丝不留。到那时，我便会低下头喃喃自语:这场景，我好像在...</p>
              <a class="author" target="_blank" href="/u/9c4c4308b499?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/2805106/6e7cd391-178f-468a-ab1d-38c4b675b5dd.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">呆若眉</span>
</a>            </div>

            <div class="note have-img">
              <a class="cover" target="_blank" href="/p/610ffd9171f6?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <img src="//upload-images.jianshu.io/upload_images/5692648-21807319d7be0ad5.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/300/h/240" alt="240" />
</a>              <a class="title" target="_blank" href="/p/610ffd9171f6?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">读书笔记《科学与宗教的领地》</a>
              <p class="description">  作者从一个比喻开始: 如果有位历史学家说:以色列和埃及在1600年爆发了一场此前为止的战争。那么这种说法是可笑的，因为1600年并没有以色列和埃及这两个国家，否认1600年的以色列并不意味着否认目前该国领土的存在，我们不能用现在的地图误用于过去的领土。 同样，对科学与宗...</p>
              <a class="author" target="_blank" href="/u/77dd948260ac?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/5692648/38b08c3c-0984-404b-8834-da1475525963.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">飞鸟和游鱼</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/46101bc4b6b8?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">弹唱词(别后)-罗大佑</a>
              <p class="description">2014.6.4 地址手指勾一勾两人心在此.眼神兜一兜可爱的样子.转身掉头去谁的俏身影.别时多珍重别后见真情.嘿呦哼嘿呦天地的真情.嘿呦哼嘿呦天地的真情.人在世间生谁无亲父母血肉身连心养大焉知苦同在世间生同耕世上土同担日月天同甘人世福嘿呦哼嘿呦天地的赐福嘿呦哼嘿呦天地的赐福...</p>
              <a class="author" target="_blank" href="/u/b9d795879d58?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/6229170/1e75392e-f2ba-4366-9404-d008c0eb2123?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">林大猴</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/c3a397bc32ea?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">20160331直播培训心得 润华天众李嘉乐</a>
              <p class="description">感谢分销中心领导和总部老师的信任，给我机会参加内训师讲竞品直播，一千个人眼中有一千个哈姆雷特,一千个上汽大众内训师眼中机油一千种竞品对比培训方法，具体怎么向各位同仁展示我们区域的竞品对比培训，就是我们此次直播的目的。 通过参与直播培训的准备工作，我收获良多，台上的每一分钟，...</p>
              <a class="author" target="_blank" href="/u/448a368a9ae6?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/1835917/925c3451f7f6?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">李老师叨逼叨</span>
</a>            </div>

            <div class="note ">
                            <a class="title" target="_blank" href="/p/7edccce6ca50?utm_campaign=maleskine&amp;utm_content=note&amp;utm_medium=seo_notes&amp;utm_source=recommendation">006 “学习”简史</a>
              <p class="description">推荐阅读时间5分钟 01 一个完整的知识学习闭环，包括知识采集、个人认知、建立连接和践行反馈四个过程，而它们又分别代表着信息输入、信息处理、信息输出和信息反馈的四个阶段。 问题导向、针对性的知识采集；目标导向、快速转化为个人认知；精简动作、高效地建立连接；先做后想、用知识短...</p>
              <a class="author" target="_blank" href="/u/dbce146f85c1?utm_campaign=maleskine&amp;utm_content=user&amp;utm_medium=seo_notes&amp;utm_source=recommendation">
                <div class="avatar">
                  <img src="//upload.jianshu.io/users/upload_avatars/1697016/5d9c9453-f4cf-4229-b93e-7ac3e25a9c8e.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/48/h/48" alt="48" />
                </div>
                <span class="name">Xiri_M</span>
</a>            </div>
      </div>
'''

img_url_list = []
# 匹配文章中图片的url
match_obj = re.findall(r'<img.*?>', text)
for img_label in match_obj:
    print(img_label)  # img标签
    for img_url in re.findall(r'src=(.+?\.jpg)', img_label):
        img_url_list.append(img_url)
        print(img_url)  # 图片url

