##˵��

��Կ��ɾ��������������

�й�API�������[API�ĵ�](https://github.com/fffonion/maClient/blob/master/API Document.md)

##����

    maclient_cli.py
    maclient_cli.py [config file]
    maclient_cli.py [config file] [task]/[commands]

##CONFIG.INI�ļ�˵��

����config.ini���Բο�config_sample.ini

***

###account_?

?��ѡcn,cn2,tw�ֱ��Ӧ����1��������2����̨��

session���ù���


###carddeck

####�����б�

ֵ��ѡ��Ƭid���߿�Ƭ���к�

�磺

    factor=124 #ѡ��С��Ů
    factor=93714777,54276719 


###system

####server

ѡ������ѡcn��cn2��tw

####loglevel

��Ļ�����־���𣬿�ѡ0-6���ӷ��͵����

####taskname

��ʾ��Ҫ����ִ�е��������ƣ�tasker�У���|�ָ�

####try_factor_time

��ˢ����ս�б�Ĵ�����0Ϊ����

####factor_sleep

ˢ�б�ļ��(��)

####explore_sleep

ˢ�ؾ��ļ��(��)

####fairy_battle_times

ˢ�����б����

####fairy_battle_sleep

ˢ�����б���(��)����ʱ�����ã�����0-5��ÿ5��ˢ��һ�Σ�5-10��ÿ2��ˢ��һ�Σ� 0,5,5|5,10,2�������ڷ�Χ�ڣ�Ĭ��1.5��

####auto_explore

�Ƿ��Զ�ѡ���ؾ�(����explore_area��explore_floor����)����Ϊ1

####auto_green_tea,auto_red_tea

�����ҩ��������ǰ���������Զ�����ʱ����������Ϊ0�������AP/BC����ʱֱ���˳�

####auto_red_tea_level

�Զ��ҩ����1.���������ľ����Զ��ҩ��2.��������������Ҳ�ҩ��0.��Զ���ҩ(BC�����������

####strict_bc

�ϸ�BCģʽ, ��ʱ����ǰBC���ڿ���costʱ��ΪBC����(ֻӰ������ս)

####auto_sell_card

����200�����Ƿ��Զ�����������select_card_to_sell����

####auto_fp_gacha

��㵽9900���Ƿ��Զ�ת��

####fp_gacha_bulk

�Ƿ�������ת����һ��10��

####auto_build

�Ƿ��Զ��ϳ���ͬ��Ƭ��Ĭ��Ϊ1��ֻӰ��̽����ת���е�һ��/���ǿ�

####delay

����POST�ӳ٣�Ĭ�Ϲرգ���Ϊ0ʱ����ʾWARNING

####auto_fairy_rewards

�Զ���ȡ��������

####sell_card_warning

�������ѣ�������2:ȫ���� ��1:R+���ѣ�0:������(��ʱֻ��R���¿�)

####del_friend_day

ɾ����������û���ߵĺ���


###tasker

���Խ������������ʽ��ÿ�����ʽ��|�ָ���������ÿո�ָ�����Ͳ�����

��ѡ��

��½login/l, ���ÿ��� set_card/sc,����ս factor_battle/fcb,�ؾ�̽�� explore/e,ˢ�б��е����� fairy_battle/fyb,�ҩ red_tea/rt,�ҩ green_tea/gt,�Զ����� sell_card/slc,�����˺����� set_server/ss,������� friend/f,ת��gacha/g

��t:��ͷ��ִ������

����explore��sell_card��ɸ�������ָ��������������condition�е�����ִ��;factor_battle��ѡ���� ���BC��Ĭ��Ϊ0��fairy_battle��ѡ���� ѭ��������Ĭ�ϰ���config����ָ���Ĵ���

�磺

    login heheh 123456 #��½ 
    set_server cn|set_card factor|factor_battle #���ù�������������ս���飬Ȼ������ս
    ss cn|sc factor|fcb #ͬ��
    explore '���R�º͍u' in area.name #̽���ؾ����ư���'���R�º͍u' 


###condition
ָ������ʲô����ʱ��ʲô��

ȫ�ֿ��õ�����

    hour ��ǰ(24Сʱ�Ƶ�)Сʱ
    minute ��ǰ����
    BC ʣ��bc
    AP ʣ��ap
    G ���
    FP �������
    FAIRY_ALIVE �Լ��������Ƿ���

####factor
����ս������ı��ʽ

������

star��cid���ֱ��Ӧͷ��������Ϳ�Ƭid

eg:

    start ==1 or star ==2��star in [1,2] #��ƬΪһ�ǻ�����
    cid in [124,8,256] #�ӳ���ƬidΪ124,8��256��

####explore_area
ѡ���ؾ�����ı��ʽ

������area

���ԣ�

��ؾ� IS_EVENT, ÿ���ؾ� IS_DAILY_EVENT,δˢ�� NOT_FINNISHED,�ؾ����� name

eg.��

    area.IS_EVENT and area.NOT_FINNISHED��#�����һ��û��ɵĻ�ؾ�
    area.name == ' �WУ�Ęǽ���' #���� ѧУ��¥����

####explore_floor
ѡ���������ı��ʽ

������floor

���ԣ�

δˢ�� NOT_FINNISHED, AP���� cost

eg.��

    floor.cost<6 and floor.NOT_FINNISHED #��û��ɵ���costС��6�ĵ�����

####fairy_select
�����б����ʲô����Ҫ��

������fairy

���ԣ�

���ҿ��� IS_MINE,ʣ��ʱ�� LIMIT(��λΪ��),û��� NOT_BATTLED,�ȼ� lv,�Ƿ���� IS_WAKE,�Լ��������Ƿ񻹻��� STILL_ALIVE

eg.��

    not fairy.IS_MINE and fairy.LIMIT<600 and fairy.NOT_BATTLED #�����ҷ��ֵģ�ʣ��ʱ��Ϊ10���ӵģ���û���������

####fairy_select_carddeck
����ʲô��������ʱѡ��ʲô���Ŀ���

������fairy

���ԣ�

lv,hp,name,IS_MINE,�Լ��������Ƿ񻹻��� STILL_ALIVE, ʣ��ʱ�� TIME_LIMIT(��λΪ��)

ֻ��ʹ��and or���ʽ ��if else���ʽ����Ƕ�ף���������������ţ�����carddeck�и���������ʹ��'no_change'��ʾ�����Ŀ���

eg.��

    fairy.hp>200000 and 'tiandao' or 'full' Ҳ��д�� 'tiandao' if fairy.hp>200000 else 'full'��#����hp>200000�������ÿ���tiandao��������full
    'no_change' #���ı�

####select_card_to_sell
�Զ���������Щ

������card

���ԣ�

star,lv,���к� sid,��Ƭ��� cid�������۸�price

eg��

    card.star in [1,2] and card.lv<5 and card.cid != 124 #1��2�� lv5һ�µĿ��Ҳ���С��Ů:

ע��
���Զ��ų������ж����������ѡ��R�����ϵĿ����������ʾȷ��