file_template=\
'''
nnoremap u :vsc Debug.SetCurrentStackFrame %(next)d<CR>:source /Users/swd/vsvim_single_key_debug/stack_commands_%(next)d.vimrc<CR>
nnoremap d :vsc Debug.SetCurrentStackFrame %(prev)d<CR>:source /Users/swd/vsvim_single_key_debug/stack_commands_%(prev)d.vimrc<CR>
'''
file_name_template='stack_commands_%(frame)d.vimrc'
for i in range(1,50):
    file_name=file_name_template % {'frame': i}
    with open(file_name,'w') as f:
        if i==1:
            f.write(file_template % {'next':i+1,'prev':i})
        else:
            f.write(file_template % {'next':i+1,'prev':i-1})
