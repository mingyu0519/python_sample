#!/usr/bin/env python
# -*- coding: utf-8 -*-

from locust import *

class mytest(TaskSet):
    @task(weight=1)
    def transaction_1(self):
        with self.client.get(name='获取学校', url='http://tieba.baidu.com/', catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure('error')


class myrun(HttpLocust):
    task_set = mytest
    min_wait = 100
    max_wait = 1000
