#-*-coding:utf-8-*- 
import db
from error.dbexcept import *
import logging


def _params2string(obj,joins,**args):
		params=[]
		for v,k in args.iteritems():
			if obj.__mapping__.has_key(v):
				params.append(v+'=\''+str(k)+'\'')
			else :
				raise ColumnNotExistsError('Column (%s) not exists'%v)
		return joins.join(params)
		
class Field(object):
	def __init__(self,column_type,not_null=True,primary_key=False,default=None,updatable=True):
		self.column_type=column_type
		self.not_null=not_null
		self.primary_key=primary_key
		self.default=default
		self.updatable=updatable

	def __str__(self):
		return '<%s:%s>'%(self.__class__.__name__,self.name)

class BooleanField(Field):
	def __init__(self,not_null=True,primary_key=False,default=0,updatable=False):
		super(BooleanField,self).__init__('boolean',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)	

	
class StringField(Field):
	def __init__(self,not_null=True,primary_key=False,default='',updatable=True,ddl='varchar(50)'):
		super(StringField,self).__init__(ddl,not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)

class TextField(Field):
	def __init__(self,not_null=True,primary_key=False,default='',updatable=True):
		super(TextField,self).__init__('text',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)
	
class IntegerField(Field):
	def __init__(self,not_null=True,primary_key=False,default=0,auto_increment=False,updatable=True):
		super(IntegerField,self).__init__('bigint',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)
		self.auto_increment=auto_increment

class FloatField(Field):
	def __init__(self,not_null=True,primary_key=False,default=0.0,updatable=True):
		super(FloatField,self).__init__('real',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)
	
class DateField(Field):
	def __init__(self,not_null=True,primary_key=False,default='0000-00-00',updatable=True):
		super(DateField,self).__init__('date',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)	
		
class DatetimeField(Field):
	def __init__(self,not_null=True,primary_key=False,default='0000-00-00 00:00:00',updatable=False):
		super(DatetimeField,self).__init__('datetime',not_null=not_null,primary_key=primary_key,default=default,updatable=updatable)	
		
class ModelMetaclass(type):
	def __new__(cls,name,base,attrs):
		if name=='Model':
			return type.__new__(cls,name,base,attrs)
		__mapping__=dict()
		attrs['__primary_key__']=[]
		for k,v in attrs.iteritems():
			if isinstance(v,Field):
				#print('Found mapping: %s =>%s'%(k,v))
				v.name=k
				__mapping__[k]=v
				if v.primary_key==True:
					#print('primary_key: %s'%v.name)
					attrs['__primary_key__'].append(v.name)
		for k,v in __mapping__.iteritems():
			attrs.pop(k)
		attrs['__mapping__']=__mapping__
		if not attrs.has_key('__table__'):
			attrs['__table__']=name
		return type.__new__(cls,name,base,attrs)
		

class Model(db.Dict):
	__metaclass__=ModelMetaclass
	
	def __init__(self,**kw):
		super(Model,self).__init__(**kw) 
        
	def save(self):
		fields =[]
		params=[]
		args=[]
		for k,v in self.__mapping__.iteritems():
			fields.append(v.name)
			params.append('?')
			args.append(getattr(self,k,None))
		sql='insert into %s (%s) values(%s)'%(self.__table__,','.join(fields),','.join(params))
		print('SQL:%s'%sql)
		print('Args: %s'%str(args))
	
	def insert(self):
		params={}
		for k,v in self.__mapping__.iteritems():
			if isinstance(v,IntegerField) and v.auto_increment:
				continue
			if not hasattr(self,v.name) and not v.default==None:
				default=v.default()if hasattr(v.default,'__call__') else v.default
				setattr(self,k,default)
				params[v.name]=getattr(self,k)
				continue
			elif v.not_null and not hasattr(self,v.name):
				raise NullError('Field (%s) is not null,but its value is null'%v.name)
				return self
			#print(v.name+v.default)
			params[v.name]=getattr(self,k)
		db.insert(self.__table__,**params)
		return self
		
	def update(self):
		if not hasattr(self,'__primary_key__') or not len(self.__primary_key__):
			raise PKIsNullError('primary key( %s ) is null'%v.name)
			return 0
		
		params=[]
		primarykeys=[]
		for k,v in self.__mapping__.iteritems():
			if self.__primary_key__.count(v.name):
				if not hasattr(self,k):
					raise PKIsNullError('primary key( %s ) is null'%v.name)
					return 0
				primarykeys.append(v.name+'=\''+str(getattr(self,k))+'\'')
			elif not v.updatable:
				continue
			elif hasattr(self,k):
				params.append(v.name+'=\''+str(getattr(self,k))+'\'')
		if not len(primarykeys) or not len(params):
			return 0
		sql='update %s set %s where %s'%(self.__table__, ' , '.join(params), ' and '.join(primarykeys))
		return db.update(sql)
	
	def update_by(self,**args):
		params=[]
		for k,v in self.__mapping__.iteritems():
			if not v.updatable:
				continue
			if not self.__primary_key__.count(v.name) and hasattr(self,k):
				params.append(v.name+'=\''+str(getattr(self,k))+'\'')
		if not len(params):
			return 0
		sql='update %s set %s where %s'%\
		(self.__table__,' , '.join(params),_params2string(self,' and ',**args))
		#print(sql)
		return db.update(sql)
	
	def delete(self):
		params={}
		for k,v in self.__mapping__.iteritems():
			if self.__primary_key__.count(k) and hasattr(self,k):
				params[k]=getattr(self,k)
		pks=_params2string(self,' and ',**params)
		sql='delete from %s where %s'%(self.__table__,pks)
		return db.update(sql)
		
	@classmethod
	def get(cls,**pk):
		#pks=[]
		#for v,k in pk.iteritems():
		#	pks.append(v+'=\''+str(k)+'\'')
		if not len(pk):
			return None
		sql='select * from %s where %s limit 1'%(cls.__table__,_params2string(cls,' and ',**pk))#' and '.join(pks)
		data=db.select_one(sql)
		return cls(**data) if data else None
	
	@classmethod
	def find_first(cls,**pk):
		return cls.get(**pk)
		
	@classmethod
	def find_all(cls,**pk):
		if not len(pk):
			data=db.select('select * from %s'%cls.__table__)
			return [cls(**x) for x in data] if len(data) else None
		#pks=[]
		#for v,k in pk.iteritems():
		#	pks.append(v+'=\''+str(k)+'\'')
		sql='select * from %s where %s'%(cls.__table__,_params2string(cls,' and ',**pk))#' and '.join(pks)
		data=db.select(sql)
		return [cls(**x) for x in data] if len(data) else None
		
	@classmethod
	def raw_find(cls,where=None,*args):
		if where == None:
			return cls.find_all()
		if not isinstance(where,basestring):
			raise WhereClauseError('where clause is not a string')
			return None
		data=db.select('select * from %s %s'%(cls.__table__,where),*args)
		return [cls(**x) for x in data] if len(data) else None
		
	@classmethod
	def find_by(cls,**param):
		if not len(param):
			return cls.find_all()
		if  not param.has_key(orderby):
			raise OrderByNotDefined('order by not defined!')
			return None
		pks=[]
		order=''
		orderby=''
		for v,k in param.iteritems():
			if v=='order':
				order=param.pop(v)
				continue
			if v=='orderby':
				orderby=param.pop(v)
				continue
			pks.append(v+'=\''+str(k)+'\'')
		if not len(order):
			order='desc'
		if not len(pks):
			sql='select * from %s order by %s %s'%(cls.__table__,orderby,order)
		else:
			sql='select * from %s where %s order by %s %s'%(cls.__table__,' and '.join(pks),orderby,order)
		data=db.select(sql)
		return [cls(**x) for x in data] if len(data) else None
		
		
	@classmethod
	def count_all(cls):
		sql='select count(*) from %s'%(cls.__table__,)
		return db.select_int(sql)
		
		
	@classmethod
	def count_by(cls,**args):
		params=[]
		for v,k in args.iteritems():
			params.append(v+'=\''+str(k)+'\'')
		sql='select count(*) from %s where %s'%(cls.__table__,' and '.join(params))
		return db.select_int(sql)
	
	@classmethod
	def createifnotexists(cls,**args):
		content=[]
		mapping=cls.__mapping__
		for k,v in mapping.iteritems():
			ct=k+' '+v.column_type
			if v.not_null:
				ct+=' NOT NULL '
			if v.default and not hasattr(v.default,'__call__'):
				ct=ct+'DEFAULT \''+str(v.default)+'\''
			if hasattr(v,'auto_increment') and v.auto_increment:
				ct+=' auto_increment'
			content.append(ct)
		content.reverse()
		primary_key=cls.__primary_key__
		if len(primary_key):
			prm='primary key ('+','.join(primary_key)+')'
			content.append(prm)
		params=[]
		for v,k in args.iteritems():
			params.append(v+'=\''+str(k)+'\'')
		sql="""create table if not exists %s(\n%s\n)default charset=utf8 %s;"""%(cls.__table__,',\n'.join(content),' '.join(params))
		#print(sql)
		db.update(sql)
		
	@classmethod
	def createifexists(cls,**args):
		db.update('drop table if exists %s'%cls.__table__)
		cls.createifnotexists(**args)
	
if __name__=='__main__':
	class User(Model):
		id=IntegerField('id')
		name=StringField('name')
		email=StringField('email')
	import debug	
	u=User(id=123,name='ryan',email='exapmle@example.com')
	u.save()
	data=debug.Debug(u,showprivate=True).simple().html()
	with open('C:\\Users\\Administrator\\Desktop\\test.html','w+')as f:
		f.write(data)
	
