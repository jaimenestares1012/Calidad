from io import BytesIO  # nos ayuda a convertir un html en pdf
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa
from io import BytesIO
# se crea la clase render
def render_to_pdf(template_src, context_dict={}):
    # se define donde se renderizara
    template = get_template(template_src)
    # se inicializa
    html =template.render(context_dict)
    # se le da la estuctura
    result=BytesIO()
    # se transforma
    pdf=pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    # se hace la condicional
    if not pdf.err:
        # se retorna el response
        return HttpResponse(result.getvalue(), content_type='applicacion/pdf')
    # se retorna un none
    return None