import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from JobCrawler.items import JobItem


class JobsSpider(CrawlSpider):
    name = "jobsdetail"
    allowed_domains = ["merojob.com"]
    start_urls = ["http://www.merojob.com/search-new/index.php?SeaOpt=basic&category=IT%20&%20Telecommunication#search"]
    # start_urls = ["http://www.merojob.com/hotjob/Core_Dreams_Innovations_HJP_2016_Jan_27.html"]
    # rules = [
    #     Rule(
    #         LxmlLinkExtractor(
    #             allow=(),
    #             deny=(),
    #             restrict_xpaths=(
    #                 '//div[@id="searchCont"]//a[@class="thumbnail spacebot"]'
    #             )
    #         ),
    #         callback="parse_jobs",
    #         follow=True,
    #     )
    # ]

    def parse_start_url(self, response):
        all_links = []
        full_url = "http://www.merojob.com/hotjob/Core_Dreams_Innovations_HJP_2016_Jan_27.html"
        # print("full url", full_url)
        my_request = scrapy.Request(
            full_url,
            self.parse_jobs
        )
        all_links.append(my_request)
        return all_links

    def parse_jobs(self, response):
        # print "response", response, 'endresponse'
        sel = Selector(response)

        job_details = {}
        job_detail_overview = {}

        if response.url == 'http://www.merojob.com/hotjob/Core_Dreams_Innovations_HJP_2016_Jan_27.html':
            # job_description = sel.xpath('//div[@id="content_newa"]').extract()
            print "core dream entered"
            job_title = sel.xpath('//h1[@class="h"]/text()').extract()
            
            if len(job_title) != 0:
                # print "job title no zero"
                for each in range(1,13):

                    my_data = sel.xpath('//dt['+str(each)+']/text()').extract()
                    if len(my_data) != 0:
                    # my_real_data = sel.xpath('//dd['+ str(each) +']/strong/text()').extract()[0]
                        my_data = my_data[0][0:-1].strip().lower().replace('.','').split(" ")
                        my_data = "_".join(my_data)
                        if my_data == 'organisation' or my_data == 'apply_before':
                            # print "enter organization"
                            job_detail_overview[my_data] = sel.xpath('//dd['+ str(each) +']/strong/text()').extract()[0]
                        else:
                            job_detail_overview[my_data] = sel.xpath('//dd['+ str(each) +']/text()').extract()[0]

            # sel.xpath('//dl[@class="dl-horizontal"]').extract()
            # print "length", len(job_title)
            if len(job_title) == 0:
                # print "job title is zero"
                job_total_overview = {}
                job_data = sel.xpath('//div[@class="subcontent"]')
                # print "job_data", job_data
                no_of_job = 1
                for each in job_data:
                    job_detail_overview1 = {}
                    all_p = each.xpath('.//p/text()')
                    job_title = sel.xpath('//h1[@class="h1"]['+str(no_of_job)+']/strong/text()').extract_first()
                    # print "job title value", job_title
                    count = 1
                    for each_p in all_p:
                        each_field = each_p.extract()
                        my_data = each_field.split(":")
                        my_data_key = my_data[0].strip().lower().replace('.','').split(" ")
                        my_data_key = "_".join(my_data_key)
                        if len(my_data) > 1:
                            if len(my_data[1]) != 0:
                                # print "enter not equal to zero"
                                print "my data key is", my_data_key, my_data[1].replace('\n','').replace('\t','')
                                job_detail_overview1[my_data_key] = my_data[1].replace('\n','').replace('\t','')
                            else:
                                # print "enter equal to zero"
                                print "my data key is next", my_data_key
                                ul_field = each.xpath('.//ul['+str(count) +']/li/text()').extract()
                                job_detail_overview1[my_data_key] = ul_field
                                count = count + 1
                                pass

                        if len(my_data) == 1:
                            print "second col zero"
                    # print "job overview is", job_detail_overview1
                    # print "job title is", job_title
                    job_total_overview[job_title] = job_detail_overview1
                    no_of_job += 1

                job_title = sel.xpath('//h1[@class="h1"]/strong/text()').extract()
            # job_link = response.url
        job_details = job_total_overview[job_total_overview.keys()[0]]
        jobItem = JobItem()
        jobItem['title'] = job_total_overview.keys()[0]
        jobItem['location'] = job_details['job_location']
        jobItem['offered_salary'] = job_details['offered_salary']
        jobItem['job_description'] = job_details['job_description']
        jobItem['no_of_vacancy'] = job_details['no_of_vacancies']
        jobItem['job_specification'] = job_details['job_specifications']
        jobItem['educational_qualification'] = job_details['educational_qualification']
        jobItem['url'] = response.url
        yield jobItem
