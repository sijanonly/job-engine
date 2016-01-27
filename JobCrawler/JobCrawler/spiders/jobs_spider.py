from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from JobCrawler.items import JobItem


class JobsSpider(CrawlSpider):
    name = "jobsdetail"
    allowed_domains = ["merojob.com"]
    start_urls = ["http://www.merojob.com/search-new/index.php?SeaOpt=basic&category=IT%20&%20Telecommunication#search"]
    rules = [
        Rule(
            LxmlLinkExtractor(
                allow=(),
                deny=(),
                restrict_xpaths=(
                    '//div[@id="searchCont"]//a[@class="thumbnail spacebot"]'
                )
            ),
            callback="parse_jobs",
            follow=True,
        )
    ]
    # rules = [Rule(SgmlLinkExtractor(restrict_xpaths=('//a[@class="spacebot"]')), callback='parse_jobs')]

    # def parse_start_url(self, response):

    #     return self.parse_jobs(response)

    def parse_jobs(self, response):
        print "response", response, 'endresponse'
        sel = Selector(response)

        job_details = {}

        if response.url == 'http://www.merojob.com/hotjob/Classictech_Vacancy_HJP_22_Dec_2015.html':
            # job_description = sel.xpath('//div[@id="content_newa"]').extract()
            job_title = sel.xpath('//h1[@class="h"]/text()').extract()
            job_detail_overview = {}
            if len(job_title) != 0:
                print "job title no zero"
                for each in range(1,13):

                    my_data = sel.xpath('//dt['+str(each)+']/text()').extract()
                    if len(my_data) != 0:
                    # my_real_data = sel.xpath('//dd['+ str(each) +']/strong/text()').extract()[0]
                        my_data = my_data[0][0:-1].strip().lower().replace('.','').split(" ")
                        my_data = "_".join(my_data)
                        if my_data == 'organisation' or my_data == 'apply_before':
                            print "enter organization"
                            job_detail_overview[my_data] = sel.xpath('//dd['+ str(each) +']/strong/text()').extract()[0]
                        else:
                            job_detail_overview[my_data] = sel.xpath('//dd['+ str(each) +']/text()').extract()[0]

            # sel.xpath('//dl[@class="dl-horizontal"]').extract()
            print "length", len(job_title)
            if len(job_title) == 0:
                print "job title is zero"
                job_total_overview = {}
                job_data = sel.xpath('//div[@class="subcontent"]')
                # print "job_data", job_data
                no_of_job = 1
                for each in job_data:
                    job_detail_overview1 = {}
                    all_p = each.xpath('.//p/text()')
                    job_title = sel.xpath('//h1[@class="h1"]['+str(no_of_job)+']/strong/text()').extract()
                    count = 1
                    for each_p in all_p:
                        each_field = each_p.extract()
                        my_data = each_field.split(":")
                        my_data_key = my_data[0].strip().lower().replace('.','').split(" ")
                        my_data_key = "_".join(my_data_key)
                        if len(my_data) > 1:
                            if len(my_data[1]) != 0:
                                print "enter not equal to zero"
                                job_detail_overview1[my_data_key] = my_data[1].replace('\n','').replace('\t','')
                            else:
                                print "enter equal to zero"
                                ul_field = each.xpath('.//ul['+str(count) +']/li/text()').extract()
                                job_detail_overview1[my_data_key] = ul_field
                                count = count + 1
                                pass

                        if len(my_data) == 1:
                            print "second col zero"

                        print each_field, my_data, job_detail_overview1
                    job_total_overview[job_title] = job_detail_overview1
                    no_of_job += 1

                job_title = sel.xpath('//h1[@class="h1"]/strong/text()').extract()
            job_link = response.url
            print "parse_jobs", job_total_overview
