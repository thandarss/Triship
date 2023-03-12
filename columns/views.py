from django.shortcuts import render

def columns_view(request):
    column1_content = "Column 1 content goes here."
    column2_content = "Column 2 content goes here."
    context = {
        'column1_content': column1_content,
        'column2_content': column2_content,
    }
    return render(request, 'horizontal_columns.html', context)
