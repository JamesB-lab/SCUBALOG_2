from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from django import forms


class Post(models.Model):
    manufacture_date = models.DateField(default =None)
    stencil_number = models.CharField    (max_length=3, default=None)
    revision = models.CharField    (max_length=2, default=None)
    ZLNumber = models.CharField    (max_length=10, default=None)
    material = models.CharField    (max_length=15, default=None)
    manufacture_number = models.CharField    (max_length=10, default=None)
    thickness = models.CharField    (max_length=5, default=None)
    author = models.CharField (max_length=7, default =None)


    def __str__(self):
        return self.manufacture_date, self.stencil_number, self.revision, self.ZLNumber, self.material, self.manufacture_number, self.thickness, self.author
        

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def save(self, *args, **kwargs):
        self.extra_field = "extra field"
        #print(self.manufacture_date, self.stencil_number, self.revision, self.ZLNumber, self.material, self.manufacture_number, self.thickness, self.author)
        super().save(*args, **kwargs)
        mystring = f'{str(self.manufacture_date)},{self.stencil_number},{self.revision},{self.ZLNumber},{self.material},{self.manufacture_number},{self.thickness},{self.author}'

        print(mystring)


        try:
            stringSplit = mystring.split(",")


            dateofmanufacture = stringSplit[0]
            stencilNumber = stringSplit[1]
            revision = stringSplit[2]
            ZLNum = stringSplit[3]
            material = stringSplit[4]
            manuSN = stringSplit[5]
            thickness = stringSplit[6]


            mydict = {'DateofManufacturer': dateofmanufacture, 'StencilNumber': stencilNumber, 'Revision': revision, 'ZLNumber': ZLNum, 'Material': material, 'ManufacturerNumber': manuSN,  'Thickness': thickness}
            

            df = pd.DataFrame.from_dict(mydict, orient='index')
            df = df.transpose()
            print('Test_1')

            #SQL Connection Windows Authentication#

            Server = 'UKC-VM-SQL01'
            Database = 'ToolBank'
            Driver = 'ODBC Driver 17 for SQL Server'
            Database_con = f'mssql://@{Server}/{Database}?driver={Driver}'
            print('Test_2')

            engine = create_engine(Database_con)
            print('Test_2.5')
            con = engine.connect()
            print('Test_3')


            df.to_sql('Stencil_Bank', con, if_exists='append', index = False)
            print(f'STENCIL LOGGED TO SQL at {datetime.now()}')



        except Exception as exc:
            print(f'ERROR CONNECTING TO SQL:{exc}')
