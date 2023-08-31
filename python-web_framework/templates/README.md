Comments
To comment-out part of a line in a template, use the comment syntax which is by default set to {# ... #}. This is useful to comment out parts of the template for debugging or to add information for other template designers or yourself:

{# note: commented-out template because we no longer use this
    {% for user in users %}
        ...
    {% endfor %}
#}
Whitespace Control
In the default configuration:

a single trailing newline is stripped if present

other whitespace (spaces, tabs, newlines etc.) is returned unchanged

If an application configures Jinja to trim_blocks, the first newline after a template tag is removed automatically (like in PHP). The lstrip_blocks option can also be set to strip tabs and spaces from the beginning of a line to the start of a block. (Nothing will be stripped if there are other characters before the start of the block.)

With both trim_blocks and lstrip_blocks enabled, you can put block tags on their own lines, and the entire block line will be removed when rendered, preserving the whitespace of the contents. For example, without the trim_blocks and lstrip_blocks options, this template:

<div>
    {% if True %}
        yay
    {% endif %}
</div>
gets rendered with blank lines inside the div:

<div>

        yay

</div>
But with both trim_blocks and lstrip_blocks enabled, the template block lines are removed and other whitespace is preserved:

<div>
        yay
</div>
You can manually disable the lstrip_blocks behavior by putting a plus sign (+) at the start of a block:

<div>
        {%+ if something %}yay{% endif %}
</div>
You can also strip whitespace in templates by hand. If you add a minus sign (-) to the start or end of a block (e.g. a For tag), a comment, or a variable expression, the whitespaces before or after that block will be removed:

{% for item in seq -%}
    {{ item }}
{%- endfor %}