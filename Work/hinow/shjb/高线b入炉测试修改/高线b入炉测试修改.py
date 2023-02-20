#!/usr/bin/env python
# encoding: utf-8
# Date: 2023/02/17
# file: 高线b入炉测试修改.py
# Email:
# Author: rakiwine

import time
from util.jsonresult import BASE_DATETIME_FROMATE

from script.custom_class_zhaxian import ItemP
from util.formate_datetime import formate_datetime

if not result.has_key("item_list"):
    result["item_list"] = []
if not result.has_key("HOT_DATA"):
    result["HOT_DATA"] = []
if not result.has_key("new_num"):
    result["new_num"] = 0
if not result.has_key("online"):
    result["online"] = False
if not result.has_key("debug"):
    result["debug"] = False
if not result.has_key("redis_dict"):
    result["redis_dict"] = {}
if not result.has_key("tmp_list"):
    result["tmp_list"] = []
last_weight_timeline = int(time.time())
last_weight_timeline_publish = int(time.time())
if not result.has_key("JIN_ONE"):
    result["JIN_ONE"] = [
        {"name": HOT_MOVE_DOWN, "value": True},
        {"name": HOT_MOVE_JIN, "value": True},
        {"name": HOT_MOVE_UP, "value": True}
    ]
if not result.has_key("TUI_ONE"):
    result["TUI_ONE"] = [
        {"name": HOT_MOVE_DOWN, "value": True},
        {"name": HOT_MOVE_TUI, "value": True},
        {"name": HOT_MOVE_UP, "value": True}
    ]
SPEED_LIST = [ROLLER_SPEED_RU, ROLLER_SPEED_CHU]
MOVE_LIST = [HOT_MOVE_UP, HOT_MOVE_JIN, HOT_MOVE_DOWN, HOT_MOVE_TUI]
RU_LU_CZ_LIST = [RU_LU_CZYX, RU_LU_CZ]
HOT_LIST = [HOT_ADD, HOT_POP,HOT_FORWARD,HOT_BACK]
MESS_LIST = []
if not result.has_key("ROLLER_SPEED_RU_TYPE"):
    result["ROLLER_SPEED_RU_TYPE"] = None
if not result.has_key("ROLLER_SPEED_CHU_TYPE"):
    result["ROLLER_SPEED_CHU_TYPE"] = None

for item in result['item_list']:
    item.step_dict.clear()

def command_rulu(start_time, in_temp, weight, item):
    from util.jsonresult import BASE_DATETIME_FROMATE
    MESS_LIST.append("rulu:w:%s,t:%s" % (weight, in_temp))
    log_append("warn", 'logic', "v", u'新版判断：入炉一根:%s ; 重:%s kg; %s' % (in_temp, weight, item.toJSON()))
    if result["debug"]:
        return
    status, exceptions, datas = get_result_by_remote_consul_server(
        service_name="liyumes", url="production_manage/api/production_record_item_start",
        json_parms={"org_id_flag": org_id_flag, "in_temp": in_temp, "weight": weight,
                    "start_time": start_time.strftime(BASE_DATETIME_FROMATE),
                    "item_flag": item.item_flag})
    if status == 0 and datas["success"] is True:
        log_append("warn", 'logic', "v", u'调用入炉接口成功')
    else:
        log_append("warn", 'logic', "v", u'调用入炉接口失败')

def command_chulu(update_time, item, is_out):
    MESS_LIST.append("chulu")
    if result["debug"]:
        return
    status, exceptions, datas = get_result_by_remote_consul_server(
        service_name="liyumes", url="production_manage/api/production_record_item_out",
        json_parms={"org_id_flag": org_id_flag, "start_time": update_time.strftime(BASE_DATETIME_FROMATE),
                    "item_flag": item.item_flag,
                    "is_out": is_out})
    if status == 0 and datas["success"] is True:
        log_append("warn", 'logic', "v", u'调用出炉接口成功')
    else:
        log_append("warn", 'logic', "v", u'调用出炉接口失败')

def command_back(item_flag, update_time):
    MESS_LIST.append("back")
    log_append("warn", 'logic', "v", u'退出一根钢坯,update_time:%s' % update_time)
    if result["debug"]:
        return
    status, exceptions, datas = get_result_by_remote_consul_server(
        service_name="liyumes", url="production_manage/api/production_record_item_back",
        json_parms={"org_id_flag": org_id_flag, "item_flag": item_flag})

def save_hot_data(name, value):
    result["HOT_DATA"].insert(0, {"name": name, "value": value})
    if len(result["HOT_DATA"]) > 3:
        result["HOT_DATA"] = result["HOT_DATA"][:3]
    return single_hot_data()


def single_hot_data():
    if len(result["HOT_DATA"]) != 3:
        return None
    is_add = True
    is_jian = True
    for i in range(3):
        data = result["HOT_DATA"][i]
        add_data = result["JIN_ONE"][i]

        if data != add_data:
            is_add = False
            break
    if is_add:
        return True
    for i in range(3):
        data = result["HOT_DATA"][i]
        jian_data = result["TUI_ONE"][i]
        if data != jian_data:
            is_jian = False
            break
    if is_jian:
        return False
    return None

def middle_list_number(l):
    if l:
        l.sort()
        if len(l) % 2 == 1:
            v = l[(len(l) - 1) / 2]
        else:
            v = int((l[len(l) / 2 - 1] + float(l[len(l) / 2])) / 2)
        return v
    else:
        return None

def max_list_number(l):
    if l:
        l.sort()
        if len(l) == 1:
            v = l[0]
        else:
            v = l[-1]
        return v
    else:
        return None

def check_weight_single():
    if result["debug"]:
        return
    try:
        if int(time.time()) - last_weight_timeline_publish > 20:
            last_weight_timeline_publish = int(time.time())
            log_append(org_id_flag, last_weight_timeline, int(time.time()), 1)
            channel_commend("weight_single", result["org_id"], {"last_timeline": result["last_weight_timeline"],"now_timeline": int(time.time())})
    except:
        pass


def debug_print_speed_type(update_time):
    if result["debug"]:
        print "1:%s, 2:%s" % (result["ROLLER_SPEED_RU_TYPE"], result["ROLLER_SPEED_CHU_TYPE"])
    log_append("warn", 'logic', update_time,
               u'入炉悬臂：%s，出炉悬臂：%s' % (result["ROLLER_SPEED_RU_TYPE"], result["ROLLER_SPEED_CHU_TYPE"]))


def tiaozheng_step():
    try:
        in_l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False and x.step <= MAX_STEP + 1]
        in_step = set([x.step for x in in_l])
        if len(in_step) != len(in_l):
            t = in_l[-1].step
            in_l.reverse()
            for item in in_l:
                if item.step < t:
                    item.step = t
                    t += 1
                elif item.step > t:
                    t = item.step + 1
    except:
        send_sentry(u'入炉脚本，调整step错误')


def create_new_item(ru_lu=None, weight=0, create_time=None):
    import datetime
    tiaozheng_step()
    item = ItemP(ru_lu=ru_lu, create_time=create_time)
    item.weight = weight
    result["new_num"] += 1
    if result["new_num"] > 300:
        result["new_num"] = 1
    item.index = result["new_num"]
    update_time = datetime.datetime.now()
    log_append("warn", 'logic', "v", u'脚本第%s根支:,updatetime:%s' % (result["new_num"],update_time))
    return item


def create_item_by_weight(value, update_time):
    tui_list = [x for x in result["item_list"] if x.ru_lu is None and x.is_ru is False and x.step == 0]
    if tui_list:
        item = tui_list[0]
        item.weight = value
        log_append("warn", 'logic', "v", u'获取到称重信息 %s %s' % (item, value))
    else:
        item = create_new_item(None, value, create_time=update_time)
        item.weight = value
        result["item_list"].append(item)
        log_append("warn", 'logic', "v", u'获取到称重信息 %s %s' % (item, value))
    log_append("warn", 'item', "v", item.toJSON())


def update_item_list(opc_name, item_flag, update_time):
    if opc_name is None or item_flag is None:
        return
    opc_name_list = opc_name.split(".")
    if len(opc_name_list) > 0:
        method = opc_name_list[-1]
    else:
        return

    if method == "add":
        l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False]
        item = ItemP(False)
        item.item_flag = item_flag
        item.is_ru = True
        item.step = 0
        if not l:
            result["item_list"].append(item)
        else:
            item.step = l[-1].step
            for ti in l:
                ti.step += 1
            result["item_list"].insert(result["item_list"].index(l[-1]) + 1, item)
    elif method == "pop":
        l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False]
        tl = [x for x in l if x.item_flag == item_flag]
        if tl:
            index = l.index(tl[0])
            if index:
                for i in range(index):
                    l[i].step -= 1
            for item in tl:
                result["item_list"].remove(item)
                log_append("warn", 'remove', "item", item)
    elif method == "forward":
        l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False]
        tl = [x for x in l if x.item_flag == item_flag]
        if tl:
            index = l.index(tl[0])
            if index:
                t = l[index].step
                tmp_flag_list = []
                while len([x for x in l if x.step == t and x.item_flag not in tmp_flag_list]):
                    for o in l:
                        if o.step == t and o.item_flag not in tmp_flag_list:
                            o.step += 1
                            tmp_flag_list.append(o.item_flag)
                    if t > MAX_STEP:
                        break
                    t += 1
            else:
                l[0].step += 1
    elif method == "back":
        item_flag = data.get("item_flag")
        l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False]
        tl = [x for x in l if x.item_flag == item_flag]
        if tl:
            index = l.index(tl[0])
            if index:
                t = l[index].step
                tmp_flag_list = []
                while len([x for x in l if x.step == t and x.item_flag not in tmp_flag_list]):
                    for o in l:
                        if o.step == t and o.item_flag not in tmp_flag_list:
                            if o.step == 0:
                                command_back(item_flag=o.item_flag, update_time=update_time)
                                result["item_list"].remove(o)
                                log_append("warn", 'remove', "item", o)
                            else:
                                o.step -= 1
                                tmp_flag_list.append(o.item_flag)
                    if t == 0:
                        break
                    t -= 1
            else:
                if l[0].step == 0:
                    # 删除刚入炉的这一根
                    command_back(item_flag=l[0].item_flag, update_time=update_time)
                    result["item_list"].remove(l[0])
                    log_append("warn", 'remove', "item", l[0])
                    pass
                else:
                    l[0].step -= 1
    tiaozheng_step()




for data in opc_data_list:
    if (datetime.datetime.now()-formate_datetime(data.get("time"))).total_seconds() > 60*10 :
        continue
    if data.get("type") == "status":
        continue
    name = data["opc_name"]
    value = data["value"]
    update_time = formate_datetime(data["time"])
    log_append(1, "log", "opc_name", "%s-%s-%s"%(name, update_time, value))
    if name == TMP_OPC:
        entering_tmp = int(value)
        result["tmp_list"].append((entering_tmp, update_time))
        if len(result["tmp_list"]) > 1000:
            result["tmp_list"].pop(0)
            continue
    if name in SPEED_LIST:  # 速度发生变化
        if name == SPEED_LIST[0]:  # 入炉辊道速度
            if value > 0:
                result["ROLLER_SPEED_RU_TYPE"] = True
                # 正转
            elif value < 0:
                # 入炉辊道反转
                result["ROLLER_SPEED_RU_TYPE"] = False
            else:
                # 入炉辊道定位
                result["ROLLER_SPEED_RU_TYPE"] = None
                item_l = [x for x in result["item_list"] if
                          x.ru_lu is False and x.step == 0 and x.is_ru is False]
                if item_l:
                    item = item_l[0]
                    if hasattr(item, 'tmp'):
                        tmp = item.tmp
                    else:
                        tmp = 0
                    weight = item.weight
                    item.is_ru = True
                    command_rulu(start_time=update_time, in_temp=tmp, weight=weight, item=item)
                    log_append('logic', u'入炉辊道定位成功 %s，完成钢坯入炉' % (item.toJSON()), update_time, 2)
                else:
                    log_append('logic', u'入炉辊道定位成功，找不到合适的钢坯进行入炉', update_time, 2)
        elif name == SPEED_LIST[1]:  # 出炉辊道速度
            if value > 0:
                result["ROLLER_SPEED_CHU_TYPE"] = True
                # 正转
            elif value < 0:
                # 出炉辊道反转
                result["ROLLER_SPEED_CHU_TYPE"] = False
            else:
                # 出炉辊道定位
                result["ROLLER_SPEED_CHU_TYPE"] = None
                item_l = [x for x in result["item_list"] if x.is_chu_roller is False and x.is_chu is False
                          and x.chu_lu is None and x.is_chu_back is True]
                if item_l:
                    item = item_l[0]
                    item.is_chu_roller = True
        continue
    if name in MOVE_LIST and value:
        jin_or_tui = save_hot_data(name=name, value=value)
        log_append(1, "log", "jin_or_tui", jin_or_tui)
        if jin_or_tui is True:
            num = 0
            l = []
            for item in result["item_list"]:
                if item.step <= MAX_STEP and item.is_ru is True and item.is_chu is False:
                    item.step += 1
                    num += 1
                    l.append(item.index)
                    #item.step_dict[item.step] = update_time.strftime(BASE_DATETIME_FROMATE)
                if item.step > MAX_STEP and item.is_chu is False:
                    item.is_chu_roller = True
                if item.step > 0:
                    item.is_ru_roller = False
            item_l = [x for x in result["item_list"] if x.is_ru is True and x.is_chu is False and x.step > MAX_STEP]
            if len(item_l) > 1:
                result["item_list"].remove(item_l[0])
                log_append("warn", 'remove', "item", item_l[0])
            out_l = ["%s:%s" % (x.index, x.step) for x in result["item_list"] if x.is_chu is True]
            pre_out_l = ["%s:%s" % (x.index, x.step) for x in result["item_list"] if
                         x.is_ru is True and x.is_chu is False and x.step > MAX_STEP]
            log_append(1, "log", "pre_out_tl", 111)
            pre_out_tl = [x for x in result["item_list"] if
                          x.is_ru is True and x.is_chu is False and x.step > MAX_STEP]
            log_append(1,"log","pre_out_tl",222)
            log_append(1, "log", "pre_out_tl", pre_out_tl)
            if len(pre_out_tl) > 1 and pre_out_tl[1] in result["item_list"]:
                result["item_list"].remove(pre_out_tl[1])
                log_append("warn", 'remove', "item", pre_out_tl[1])
            if len(pre_out_tl) > 1 and pre_out_tl[1] in result["item_list"]:
                result["item_list"].remove(pre_out_tl[1])
                log_append("warn", 'remove', "item", pre_out_tl[1])
            in_l = ["%s:%s" % (x.index, x.step) for x in result["item_list"] if
                    x.is_ru is True and x.is_chu is False and x.step <= MAX_STEP + 1]
            pre_in_tl = [x for x in result["item_list"] if x.is_ru is False]
            if len(pre_in_tl) > 1 and pre_in_tl[1] in result["item_list"]:
                result["item_list"].remove(pre_in_tl[1])
                log_append("warn", 'remove', "item", pre_in_tl[1])
            pre_in_tl = [x for x in result["item_list"] if x.is_ru is False]
            if len(pre_in_tl) > 1 and pre_in_tl[1] in result["item_list"]:
                result["item_list"].remove(pre_in_tl[1])
                log_append("warn", 'remove', "item", pre_in_tl[1])
            pre_in_l = ["%s:%s" % (x.index, x.step) for x in result["item_list"] if x.is_ru is False]
            log_append("warn", 'logic', "v", u'发生一次步进梁向前移动钢坯，有%s根钢坯前进1步,炉外%s根，炉内%s跟，正在入炉%s' % (
                num, len(out_l), len(in_l), len(pre_in_l)))
            log_append("warn", 'logic', "v", "出炉：%s, %s," % (len(out_l), out_l))
            log_append("warn", 'logic', "v", "出炉悬臂：%s, %s," % (len(pre_out_l), pre_out_l))
            log_append("warn", 'logic', "v", "炉内：%s, %s," % (len(in_l), in_l))
            log_append("warn", 'logic', "v", "炉前：%s, %s," % (len(pre_in_l), pre_in_l))
        if jin_or_tui is False:
            num = 0
            for item in result["item_list"]:
                if item.is_chu_roller is False and item.is_chu is False:
                    if item.step > 0:
                        item.step -= 1
                        num += 1
                        #item.step_dict[item.step] = update_time.strftime(BASE_DATETIME_FROMATE)
                    if item.step == 0:
                        item.is_ru_roller = True
                elif item.is_chu_roller is True and item.is_chu is False:
                    item.is_chu_roller = False
            log_append("warn", 'logic', "v", u'发生一次步进梁向后移动钢坯，有%s根钢坯后退1步,如果数量不对，可能是因为程序刚刚启动。' % (num,))
        continue

    if name in RU_LU_CZ_LIST:
        if name == RU_LU_CZYX:
            result["RU_LU_CZYX"] = value
        if name == RU_LU_CZ:
            result["RU_LU_CZ"] = value
        if result.get("RU_LU_CZYX") is True and "RU_LU_CZ" in result:
            create_item_by_weight(result["RU_LU_CZ"], update_time)
        continue
    #debug_print_speed_type(update_time)
    if name == RU_LU:
        if value:
            if result["ROLLER_SPEED_RU_TYPE"] in [True, None]:
                tui_list = [x for x in result["item_list"] if
                            x.ru_lu in [None, True] and x.is_ru is False and x.step == 0]
                #log_append(1, "log", "tui_list", tui_list)
                if not tui_list:
                    no_ru_list = [x for x in result["item_list"] if
                                x.ru_lu is False and x.is_ru is False and x.step == 0]
                    if not no_ru_list:
                        item = create_new_item(value, 0, update_time)
                        result["item_list"].append(item)
                        log_append('logic', u'入炉口检测到一根新钢坯 %s' % (item.toJSON(),), update_time, 2)
                    else:
                        log_append(1, "log", u"检测到一根在入炉悬臂的钢坯", no_ru_list)
                        continue
                else:
                    log_append(1, "log", "tui_list", tui_list)
                    item = tui_list[0]
                    item.ru_lu = True
                    try:
                        if item.create_time > update_time:
                            item.create_time = update_time
                    except:
                        pass
                    log_append('logic', u' %s:%skg' % (item.toJSON(), item.weight), update_time, 2)
                index = result["item_list"].index(item)
                if len(result["item_list"]) - index > 1:
                    try:
                        tmp_item = result["item_list"][index + 1]
                        result["item_list"].remove(tmp_item)
                        log_append("warn", 'remove', "item", tmp_item)
                    except:
                        pass
            elif result["ROLLER_SPEED_RU_TYPE"] is False:
                item_l = [x for x in result["item_list"] if x.ru_lu is False and x.is_ru is True and x.step == 0]
                if item_l:
                    item = item_l[-1]
                    item.ru_lu = True
                    item.is_ru = False
                    log_append('logic', u'入炉口检测到一根钢坯正在退炉 %s' % (item.toJSON(),), update_time, 2)
                else:
                    log_append('logic', u'找不到退炉的钢坯', update_time, 2)
        else:
            if result["ROLLER_SPEED_RU_TYPE"] is True:
                item_l = [x for x in result["item_list"] if x.ru_lu is True and x.is_ru is False and x.step == 0]
                if item_l:
                    item = item_l[0]
                    item.ru_lu = False
                    tmp_l = [x[0] for x in result["tmp_list"] if x[1] < update_time]
                    if tmp_l:
                        tmp = max_list_number(tmp_l)
                    else:
                        tmp = 0
                    result["tmp_list"] = [x for x in result["tmp_list"] if x[1] > update_time]
                    item.tmp = tmp
                    #log_append('log','logic',"tmp_list",item.tmp_list)
                    item.tmp_list = tmp_l
                    #log_append('logic', u'入炉一根钢坯，悬臂未定位 %s' % (item.toJSON(),),
                    #           update_time, 2)
                else:
                    log_append('logic', u'找不到入炉完成的钢坯', update_time, 2)

            elif result["ROLLER_SPEED_RU_TYPE"] is False:
                save_result_msg("back_1")
                item_l = [x for x in result["item_list"] if x.ru_lu is True and x.is_ru is False and x.step == 0]
                if item_l:
                    item = item_l[-1]
                    item.ru_lu = None
                    command_back(item_flag=item.item_flag,update_time=update_time)
                    tui_list = [x for x in result["item_list"] if
                                x.ru_lu is None and x.is_ru is False and x.step == 0]
                    if len(tui_list) > 1:
                        for i, o in enumerate(tui_list):
                            if i > 0:
                                result["item_list"].remove(o)
                                log_append("warn", 'remove', "item", o)
                    log_append('logic', u'入炉口检测到一根钢坯退炉完成 %s' % (item.toJSON(),), update_time, 2)
                else:
                    log_append('logic', u'找不到退炉完成的钢坯', update_time, 2)

    elif name == CHU_LU:  # 出炉口热检
        save_result_msg("出炉口热检")
        if result["ROLLER_SPEED_CHU_TYPE"] is True:
            if value:
                item_l = [x for x in result["item_list"] if
                          x.is_chu_roller is True and x.is_chu is False and x.chu_lu is None]
                if item_l:
                    item = item_l[0]
                    item.chu_lu = True
                    item.is_chu_roller = False
                    item.is_chu_back = False
                    command_chulu(update_time=update_time, item=item, is_out=True)
                    #log_append("warn", 'logic', "v", u'钢坯出炉口出炉检测 %s' % (item.toJSON(),))
                else:
                    log_append("warn", 'logic', "v", u'检测不到开始出炉的钢坯')
            else:
                item_l = [x for x in result["item_list"] if
                          x.is_chu_roller is False and x.is_chu is False and x.chu_lu is True]
                #log_append(1, "log", "item_l", item_l)
                if item_l:
                    item = item_l[0]
                    item.is_chu = True
                    item.chu_lu = False

                    index = result["item_list"].index(item)
                    if index > 2:
                        result["item_list"].pop(0)
                        result["item_list"].pop(0)
                    elif index > 1:
                        result["item_list"].pop(0)
                        #log_append("warn", 'logic', "v", u'钢坯出炉口检测到出炉 %s' % (item.toJSON()))
                    else:
                        log_append("warn", 'logic', "v", u'检测不到出炉完成的钢坯')
        elif result["ROLLER_SPEED_CHU_TYPE"] is False:
            if value:
                item_l = [x for x in result["item_list"] if
                          x.is_chu_roller is False and x.is_chu is True and x.chu_lu is False]
                if item_l:
                    item = item_l[-1]
                    item.chu_lu = True
                    item.is_chu_back = True
                    command_chulu(update_time=update_time, item=item, is_out=False)
                    #log_append("warn", 'logic', "v", u'钢坯出炉口退炉检测 %s' % (item.toJSON(),))
                else:
                    log_append("warn", 'logic', "v", u'出炉口检测不到开始退炉的钢坯')
            else:
                item_l = [x for x in result["item_list"] if
                          x.is_chu_roller is False and x.is_chu is True and x.chu_lu is True and x.is_chu_back is True]
                log_append(1, "log", "item_l", item_l)
                if item_l:
                    item = item_l[-1]
                    item.is_chu = False
                    item.chu_lu = None
                    #log_append("warn", 'logic', "v", u'钢坯出炉口检测到退炉 %s' % (item.toJSON()))
                else:
                    log_append("warn", 'logic', "v", u'出炉口检测不到退炉完成的钢坯')
    elif name in HOT_LIST:
        update_item_list(opc_name=name, item_flag=value,update_time=update_time)
    elif name == TUI_LU:
        if value:
            MESS_LIST.append("TUILU")
            item_l = [x for x in result["item_list"] if x.ru_lu is False and x.step == 0]
            if item_l:
                item = item_l[-1]
                item.ru_lu = None
                result["item_list"].remove(item)
                command_back(item_flag=item.item_flag, update_time=update_time)
                log_append("退炉一根",item, item_l, update_time)
save_result_msg(MESS_LIST)