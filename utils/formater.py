

"""
    Функция принимает текст и обрезать его до определенного размера и добавляет ... если текст сильно большой 
    Возвращает обновленную версию 
    450 макс
    
    Например
    format_text("nsdfkjgnsdkjfgksdjfgnkjsdfgnjksd") -> "nsdfkjgnsdkjfgksdjfgnk..."
    format_text("nsdfkjgnsd") -> "nsdfkjgnsd"
"""

def formater(text):
    sym = len(text)
    if sym > 450:
        new_text = ''
        for i in range(450):
            new_text += (text[i])
        new_text += '...'
        return new_text
    else:
        return text
