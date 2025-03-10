
class AmazonBooksPipeline:
    def process_item(self, item, spider):
        item['title'] = item['title']
        item['author'] =  item['author']
        item['price']=item['price']
        item['img_link']=item['img_link']
        return item
