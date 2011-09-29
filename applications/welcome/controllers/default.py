# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a samples controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################

COMING_SOON = False

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
    """
    if COMING_SOON:
        redirect(URL(r=request, f='coming_soon'))
        
    return dict(chars=['a', 'b', 'c'])
    
def coming_soon():
    form = SQLFORM.factory(db.invitation, submit_button='DREAM', formstyle='table3cols')
            
    if form.process().accepted:
        db.invitation.insert(email=form.vars.email)
        response.flash = 'You have wonderful dreams!'
    elif form.errors:
        response.flash = 'Invalid Email'
    else:
        response.flash = 'Type your email'
        
    return dict(form=form)

@auth.requires_login()

def dream():
    form = SQLFORM.factory(db.invitation, submit_button='Add Dream', formstyle='table3cols')
    return dict(form=form)

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    if COMING_SOON:
        redirect(URL(r=request, f='coming_soon'))
        
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    if COMING_SOON:
        redirect(URL(r=request, f='coming_soon'))
    return response.download(request,db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    if COMING_SOON:
        redirect(URL(r=request, f='coming_soon'))
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs bust be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    if COMING_SOON:
        redirect(URL(r=request, f='coming_soon'))
    return dict(form=crud())
