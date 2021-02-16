# # -*- coding: utf-8 -*-

# from django.http import HttpResponse
# import csv


# class ExportView():
#     def Export(request):
#     # Create the HttpResponse object with the appropriate CSV header.
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

#     writer = csv.writer(response)
#     writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
#     writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])

#     return response
    